from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from app.config import settings
from app.routes import products, services, orders, users, auth, instagram
from app.routes.quotes import router as quotes_router

# Garantir que o diretório de uploads existe
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

# Inicializar app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API para Proteus.lab - Design e Impressão 3D",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc"
)

# CORS liberado (para testar no Swagger e localmente)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(auth.router, prefix=settings.API_V1_STR, tags=["Auth"])
app.include_router(products.router, prefix=settings.API_V1_STR, tags=["Products"])
app.include_router(services.router, prefix=settings.API_V1_STR, tags=["Services"])
app.include_router(orders.router, prefix=settings.API_V1_STR, tags=["Orders"])
app.include_router(users.router, prefix=settings.API_V1_STR, tags=["Users"])
app.include_router(instagram.router, prefix=settings.API_V1_STR, tags=["Instagram"])
app.include_router(quotes_router, prefix=settings.API_V1_STR, tags=["Quotes"])

# Endpoint raiz
@app.get("/")
def root():
    return {"message": "Welcome to the Proteus.lab API"}

# Health check
@app.get("/api/health")
def health_check():
    return {"status": "ok", "version": "1.0.0"}

# Rodar localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
