from fastapi import FastAPI
from routes.conversion import router as conversion_router
from routes.statistics import router as statistics_router

app = FastAPI()

# Registrar las rutas
app.include_router(conversion_router, prefix="/api", tags=["Conversion"])
app.include_router(statistics_router, prefix="/api", tags=["Statistics"])
