FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#  Informa ao Python onde começa a raiz dos módulos (app.config, app.routes, etc.)
ENV PYTHONPATH=/app/backend

EXPOSE 8000

#  Corrige o path do módulo para rodar o FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
