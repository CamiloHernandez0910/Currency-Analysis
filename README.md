# Conversor de Monedas con FastAPI y MongoDB

## Descripción
Este proyecto es una API REST desarrollada con **FastAPI** que permite convertir monedas en tiempo real utilizando una API externa. Además, almacena las tasas de cambio mensuales en **MongoDB** para futuros análisis de la información.

## Características
- Conversión de monedas utilizando datos en tiempo real.
- Almacenamiento de tasas de cambio mensuales en MongoDB.
- Documentación automática con Swagger UI.

## Tecnologías Utilizadas
- **Lenguaje:** Python 3
- **Framework:** FastAPI
- **Base de Datos:** MongoDB
- **Cliente HTTP:** httpx
- **Servidor de Desarrollo:** Uvicorn

## Instalación y Configuración
### Prerrequisitos
- Tener **Python 3** instalado.
- Tener **MongoDB** instalado y ejecutándose localmente o en la nube (MongoDB Atlas).

### Instalación del Proyecto
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/CamiloHernandez0910/Currency-Analysis.git
   cd Currency-Analysis
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En macOS/Linux
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install fastapi uvicorn pymongo httpx datetime dotenv
   ```

4. Configurar la conexión a MongoDB en `config/setting.py`:
   ```python
   Agrega las variables de entorno correspondientes en el .env
   ```

## Uso
### Ejecutar el Servidor
```bash
uvicorn main:app --reload
```
El servidor estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Endpoints Disponibles
| Método | Ruta | Descripción |
|---------|------|-------------|
| `GET` | `/convert/?amount=10&from_currency=USD&to_currency=COP` | Convierte 10 USD a COP |
| `GET` | `/docs` | Documentación Swagger |

## Ejemplo de Respuesta
### **Conversión de moneda** (`GET /convert/?amount=100&to_currency=EUR`)
```json
{
  "amount": 100,
  "currency": "EUR",
  "converted_amount": 94.5,
  "rate": 0.945
}
```

## 👨‍💻 Contribuciones
¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:
1. Haz un **fork** del repositorio
2. Crea una nueva rama (`git checkout -b feature-nueva`)
3. Realiza los cambios y haz **commit** (`git commit -m 'Agrega nueva funcionalidad'`)
4. Haz **push** a tu rama (`git push origin feature-nueva`)
5. Abre un **Pull Request**

---
**Desarrollado con ❤️ por [HERTUQ](https://github.com/CamiloHernandez0910)** 🚀


