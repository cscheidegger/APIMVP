
# Proteus.lab API

Este repositório contém o backend API em FastAPI para a plataforma Proteus.lab de serviços de impressão 3D.

## Visão Geral

Esta API fornece endpoints para:
- Gerenciamento de produtos e serviços
- Sistema de orçamentos
- Processamento de pedidos
- Autenticação de usuários
- Integração com Instagram

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic para migrações
- Pydantic para validação de dados
- JWT para autenticação

## Requisitos

- Python 3.10 ou superior
- PostgreSQL
- Redis (para cache)

## Desenvolvimento Local

1. Clone o repositório:
   ```bash
   git clone https://github.com/cscheidegger/APIMVP.git
   cd APIMVP
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente em um arquivo `.env`:
   ```
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/proteuslab
   SECRET_KEY=your-secret-key
   ```

5. Execute as migrações do banco de dados:
   ```bash
   alembic upgrade head
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   uvicorn app.main:app --reload
   ```

7. Acesse a documentação da API em [http://localhost:8000/docs](http://localhost:8000/docs)

## Estrutura do Projeto

```
app/
├── models/        # Modelos SQLAlchemy
├── schemas/       # Esquemas Pydantic
├── routes/        # Endpoints da API
├── services/      # Lógica de negócios
├── utils/         # Funções utilitárias
├── config.py      # Configurações
├── database.py    # Configuração do banco de dados
└── main.py        # Ponto de entrada da aplicação
```

## Docker

Este projeto inclui um Dockerfile para construir e executar a API em um contêiner.

1. Construa a imagem:
   ```bash
   docker build -t proteus-api .
   ```

2. Execute o contêiner:
   ```bash
   docker run -p 8000:8000 -e DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/proteuslab proteus-api
   ```

3. Acesse a API em [http://localhost:8000](http://localhost:8000)

## Endpoints Principais

- `POST /api/auth/login` - Autenticação
- `GET /api/products` - Lista produtos
- `POST /api/quotes` - Cria orçamento
- `GET /api/orders` - Lista pedidos
- `POST /api/instagram/update` - Atualiza feed do Instagram

## Integração DevOps

Esta API é parte de uma arquitetura maior, orquestrada pelo repositório [devopsMVP](https://github.com/cscheidegger/devopsMVP), que integra:

- Frontend ([FrontMVP](https://github.com/cscheidegger/FrontMVP))
- Backend API (este repositório)
- Banco de dados PostgreSQL
- Cache Redis
- Serviço de integração com Instagram

## Licença

[MIT](LICENSE)
