# Relatório do Projeto

## Estrutura do Projeto

O projeto foi organizado seguindo as melhores práticas de desenvolvimento web, com separação clara entre frontend e backend.

### Frontend

- `index.html`: Página principal com layout responsivo
- `styles.css`: Estilos usando CSS moderno (Grid/Flexbox)
- `scripts.js`: JavaScript moderno (ES6+)

### Backend

- `app.py`: Aplicação FastAPI
- `models.py`: Modelos SQLAlchemy
- `database.py`: Configuração do banco de dados
- `seed.py`: Script para dados iniciais
- `requirements.txt`: Dependências Python

## Funcionalidades Implementadas

1. Catálogo de Produtos
   - Grid responsivo
   - Busca por nome
   - Ordenação por preço
   - Filtro por categoria

2. Carrinho de Compras
   - Adição/remoção de itens
   - Persistência no localStorage
   - Cupom de desconto (ALUNO10)
   - Modal responsivo

3. Área Administrativa
   - CRUD de produtos
   - Validações de formulário
   - Feedback visual

## Acessibilidade

1. Semântica HTML5
   - Uso apropriado de tags (`header`, `main`, `nav`, etc.)
   - Landmarks ARIA quando necessário

2. Navegação por Teclado
   - Foco visível em todos elementos interativos
   - Ordem de tabulação lógica
   - Atalhos de teclado para ações principais

3. Contraste e Legibilidade
   - Contraste mínimo de 4.5:1
   - Textos legíveis e redimensionáveis
   - Ícones com alternativas textuais

4. ARIA
   - Labels descritivos
   - Estados dinâmicos (pressed, expanded, etc.)
   - Mensagens de feedback

## API RESTful

### Endpoints

1. Produtos
   - GET /api/produtos
   - POST /api/produtos
   - GET /api/produtos/{id}
   - PUT /api/produtos/{id}
   - DELETE /api/produtos/{id}

2. Pedidos
   - GET /api/pedidos
   - POST /api/pedidos

### Status Codes

- 200: Sucesso
- 201: Criado com sucesso
- 400: Erro de validação
- 404: Recurso não encontrado
- 422: Entidade não processável
- 500: Erro interno do servidor

## Banco de Dados

- SQLite com SQLAlchemy
- Modelos bem definidos com relacionamentos
- Validações no nível do banco
- Script de seed com 20 produtos

## Desafios e Soluções

1. Acessibilidade
   - Implementação cuidadosa de ARIA labels
   - Testes com leitores de tela
   - Navegação por teclado otimizada

2. Performance
   - Carregamento otimizado de imagens
   - Paginação no backend
   - Cache no frontend

3. UX
   - Feedback visual claro
   - Mensagens de erro informativas
   - Interface intuitiva

## Melhorias Futuras

1. Autenticação de usuários
2. Histórico de pedidos
3. Sistema de avaliações
4. Mais opções de filtros
5. Relatórios administrativos
