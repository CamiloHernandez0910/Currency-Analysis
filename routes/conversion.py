from fastapi import APIRouter, HTTPException
import httpx
from datetime import datetime
from config.database import db
from config.settings import EXCHANGE_API

router = APIRouter()

@router.get("/convert/")
async def convert(amount: float, from_currency: str, to_currency: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(EXCHANGE_API)
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail="Error al obtener tasas de cambio")

            data = response.json()

            if "conversion_rates" not in data:
                raise HTTPException(status_code=400, detail="La API no devolvió las tasas de cambio")

            # Validar que ambas monedas existen en la respuesta
            if from_currency not in data["conversion_rates"]:
                raise HTTPException(status_code=400, detail=f"Moneda {from_currency} no encontrada")
            if to_currency not in data["conversion_rates"]:
                raise HTTPException(status_code=400, detail=f"Moneda {to_currency} no encontrada")

            # Obtener las tasas de cambio
            rate_from = data["conversion_rates"][from_currency]
            rate_to = data["conversion_rates"][to_currency]

            # Convertir la cantidad
            converted_amount = amount * (rate_to / rate_from)

            # Guardar en MongoDB la conversión realizada
            db["exchange_rates"].insert_one({
                "from_currency": from_currency,
                "to_currency": to_currency,
                "rate": rate_to / rate_from,
                "date": datetime.now().strftime("%Y-%m-%d")
            })

            return {
                "amount": amount,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "converted_amount": converted_amount,
                "rate": rate_to / rate_from
            }

        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error al conectarse a la API: {str(e)}")
