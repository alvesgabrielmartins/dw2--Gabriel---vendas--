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

1. [Primeira peculiaridade]
   - Descrição da implementação
   - Tecnologias utilizadas
   - Desafios encontrados

2. [Segunda peculiaridade]
   - Descrição da implementação
   - Tecnologias utilizadas
   - Desafios encontrados

## Validações

### Frontend
```javascript
// Exemplos de validações no frontend
```

### Backend
```python
# Exemplos de validações no backend
```

## Acessibilidade

1. Semântica HTML5
   - Uso apropriado de tags semânticas
   - Estrutura hierárquica clara

2. ARIA
   - Labels e descrições
   - Roles apropriadas
   - Estados dinâmicos

3. Navegação por Teclado
   - Focus visível
   - Ordem lógica de tabulação
   - Atalhos de teclado

## Como Rodar o Projeto

### Pré-requisitos
- Python 3.9+
- Node.js (opcional, para desenvolvimento frontend)
- Git

### Passos

1. Clone o repositório
```bash
git clone https://github.com/alvesgabrielmartins/dw2--Gabriel---vendas--.git
cd dw2--Gabriel---vendas--
```

2. Configure o ambiente backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Inicie o servidor backend
```bash
uvicorn main:app --reload
```

4. Acesse o frontend
- Abra o arquivo `frontend/index.html` em um navegador
- Ou use Live Server no VS Code

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

