#!/bin/bash
# Este script inicia o servidor FastAPI com Uvicorn

# Garante que estamos no diretório correto
cd /app

# Lista todos os arquivos para debugging (opcional)
echo "Conteúdo do diretório /app:"
ls -la

# Procura pelo arquivo main.py
if [ -f "main.py" ]; then
    echo "Iniciando a aplicação a partir de main.py"
    exec python -m uvicorn main:app --host 0.0.0.0 --port 8000
elif [ -f "app/main.py" ]; then
    echo "Iniciando a aplicação a partir de app/main.py"
    exec python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
else
    echo "ERRO: Arquivo main.py não encontrado"
    echo "Conteúdo do diretório atual:"
    ls -la
    echo "Conteúdo do diretório /app/app (se existir):"
    if [ -d "app" ]; then
        ls -la app
    fi
    exit 1
fi