from fastapi import FastAPI
from routes.conversion import router as conversion_router

app = FastAPI()

# Registrar las rutas
app.include_router(conversion_router, prefix="/api", tags=["Conversion"])
