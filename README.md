# Sistema de Vendas

Sistema web de vendas desenvolvido com FastAPI no backend e JavaScript puro no frontend.

## Descrição

O sistema permite gerenciar:
- Produtos
- Vendas
- Relatórios

## Estrutura do Projeto

```
.
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── requirements.txt
└── frontend/
    ├── index.html
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

## Requisitos

- Python 3.8+
- Node.js (opcional, para servir o frontend)

## Configuração e Execução

### Backend (Windows - PowerShell)

1. Abra o PowerShell e vá para a pasta `backend`:
```powershell
cd C:\Users\Pass\Downloads\biel\backend
```

2. Existe um script helper `run-dev.ps1` que automatiza os passos (recomendado):
```powershell
.\run-dev.ps1
```

3. Se preferir fazer manualmente:
```powershell
python -m venv venv
# se necessário permitir execução temporária de scripts:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install uvicorn
python seed.py
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

Observação: as rotas do backend usam o prefixo `/api` (ex.: `GET /api/produtos`).

### Frontend

Abra `frontend/index.html` diretamente no navegador, ou sirva com `http-server` (opcional):
```bash
cd frontend
npx http-server .
```

## Funcionalidades

- Cadastro e listagem de produtos
- Registro e listagem de vendas
- Interface responsiva com CSS Grid e Flexbox
- API RESTful com FastAPI
- Banco de dados SQLite com SQLAlchemy

## API Endpoints

- `GET /produtos` - Lista todos os produtos
- `POST /produtos` - Cadastra um novo produto
- `GET /vendas` - Lista todas as vendas
- `POST /vendas` - Registra uma nova venda

- Clientes
- Vendas
- Relatórios

## Como utilizar

1. Clone o repositório
2. Instale as dependências
3. Execute o projeto

## Tecnologias utilizadas

- [Liste aqui as tecnologias que serão utilizadas]

## Contribuição

Sinta-se livre para contribuir com o projeto através de Pull Requests.

## Licença

Este projeto está sob a licença MIT.
>>>>>>> d4080c9f22d22ccad204aa849ce9035ca29afdb6
