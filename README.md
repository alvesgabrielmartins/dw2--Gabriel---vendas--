# Sistema de Vendas

Sistema web de vendas desenvolvido com FastAPI no backend e JavaScript puro no frontend.

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

### Backend

1. Entre na pasta do backend:
```bash
cd backend
```

2. Crie um ambiente virtual Python:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute o servidor:
```bash
python main.py
```

O servidor estará rodando em `http://localhost:8000`

### Frontend

Para executar o frontend, você pode usar qualquer servidor HTTP simples. Uma opção é usar o módulo `http-server` do Node.js:

1. Instale o http-server globalmente (necessário apenas uma vez):
```bash
npm install -g http-server
```

2. Na pasta frontend, execute:
```bash
http-server
```

Ou simplesmente abra o arquivo `index.html` diretamente no navegador.

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
