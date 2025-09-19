# Roteiro de Execução

[seção anterior do roteiro mantida...]

# Relatório Técnico

## Arquitetura

### Diagrama de Arquitetura
```
[Frontend]  [FastAPI Backend]  [SQLAlchemy ORM]  [SQLite Database]
```

### Fluxo de Requisição
1. Frontend faz requisição HTTP
2. FastAPI recebe e valida a requisição
3. ORM (SQLAlchemy) traduz para operações SQL
4. SQLite executa as operações
5. Dados retornam pelo mesmo fluxo com transformações apropriadas

## Tecnologias e Versões

### Backend
- Python 3.9
- FastAPI 0.68.0
- SQLAlchemy 1.4.23
- SQLite 3.36.0
- Uvicorn (ASGI server)
- Python-dotenv

### Frontend
- HTML5
- CSS3 (Flexbox/Grid)
- JavaScript ES6+
- Fetch API

### Extensões VS Code Utilizadas
- Python
- SQLite Viewer
- Live Server
- Prettier
- ESLint

### Sugestões do GitHub Copilot
[Lista das principais sugestões do Copilot será adicionada durante o desenvolvimento]

## Prompts do Copilot e Código Gerado

### 1. Exemplo de Prompt
```python
# Original prompt: "crie uma função para validar o preço do produto"
```
[Código aceito/editado + explicação será adicionado durante o desenvolvimento]

[Mais 5 exemplos serão adicionados durante o desenvolvimento]

## Peculiaridades Implementadas

Implementamos as seguintes peculiaridades obrigatórias (3 de 10):

1. Acessibilidade real
   - Aplicado: `tabindex`, `aria-labels`, foco visível por CSS, contraste de cores e navegação por teclado nas ações principais (filtros, carrinho, formulários).
   - Tecnologias: HTML5, CSS (outlines e variáveis de tema), JavaScript para gerenciamento de estados ARIA.

2. Seed script com dados plausíveis
   - Aplicado: `backend/seed.py` insere ~20 produtos no banco SQLite (`app.db`).
   - Tecnologias: SQLAlchemy + script Python.

3. Filtro avançado e ordenação persistida
   - Aplicado: painel de filtros (`frontend/index.html`) com busca por nome, categoria, faixa de preço e opção "apenas em estoque"; ordenação por nome/preço com persistência via `localStorage` para manter preferência do usuário.
   - Tecnologias: JavaScript ES6 (fetch + DOM) e `localStorage`.

## Validações

### Frontend
```javascript
// Exemplos de validações no frontend
```

### Backend
```python
# Exemplos de validações no backend
```

## Acessibilidade (detalhes aplicados)

1. Semântica HTML5
   - Uso de `header`, `main`, `nav`, `section` e botões com `aria-*`.
   - Estrutura hierárquica clara e labels em formulários.

2. ARIA
   - Labels e descrições
   - Roles apropriadas
   - Estados dinâmicos

3. Navegação por Teclado
   - Focus visível por CSS (`:focus` outline)
   - Ordem lógica de tabulação e `tabindex` nos elementos interativos
   - Atalho para abrir o painel de filtros e o carrinho via teclado (configurado no JS)

## Como Rodar o Projeto (resumo)

### Pré-requisitos
- Python 3.9+
- Node.js (opcional, para desenvolvimento frontend)
- Git

### Passos (Windows - PowerShell)

1. Clone o repositório e entre na pasta:
```powershell
git clone https://github.com/alvesgabrielmartins/dw2--Gabriel---vendas--.git
cd dw2--Gabriel---vendas--
cd backend
```

2. Recomendado: execute o helper `run-dev.ps1` (ele cria venv, instala deps, roda seed e inicia o servidor):
```powershell
.\run-dev.ps1
```

3. Rotas úteis após iniciar o servidor:
- Health: `GET http://127.0.0.1:8000/health`
- Lista de produtos: `GET http://127.0.0.1:8000/api/produtos`
- Docs FastAPI: `http://127.0.0.1:8000/docs`

[Screenshots do projeto em execução serão adicionados]

## Limitações e Melhorias Futuras

### Limitações Atuais
1. [Limitação 1]
2. [Limitação 2]
3. [Limitação 3]

### Melhorias Planejadas
1. Implementação de autenticação JWT
2. Sistema de cache para melhor performance
3. Mais opções de filtros e ordenação
4. Dashboard administrativo
5. Sistema de notificações em tempo real

