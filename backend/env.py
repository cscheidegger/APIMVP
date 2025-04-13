# API
API_V1_STR=/api
PROJECT_NAME=Proteus.lab API

# Segurança (JWT)
SECRET_KEY=super-secret-key-for-dev-only
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Banco de Dados
DATABASE_URL=postgresql://postgres:postgres@db:5432/proteus_db

# CORS (para acesso do frontend)
CORS_ORIGINS=["http://localhost:3000", "http://localhost:5173"]

# Upload de arquivos
UPLOAD_DIR=uploads
MAX_UPLOAD_SIZE=52428800  # 50 MB
ALLOWED_EXTENSIONS=[".stl", ".obj", ".3mf"]

# E-mail (desativado por padrão)
EMAIL_ENABLED=False
EMAIL_SENDER=noreply@proteuslab.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_USE_TLS=True

# Integração com Google Drive
GDRIVE_ENABLED=False
GDRIVE_FOLDER_ID=

# URL do Frontend
FRONTEND_URL=http://localhost:5173
