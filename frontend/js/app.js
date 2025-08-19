// Configuração da API
const API_URL = 'http://localhost:8000';

// Funções de utilidade
async function fetchAPI(endpoint, options = {}) {
    const response = await fetch(`${API_URL}${endpoint}`, {
        headers: {
            'Content-Type': 'application/json',
        },
        ...options
    });
    if (!response.ok) {
        throw new Error(`Erro na requisição: ${response.statusText}`);
    }
    return response.json();
}

// Funções para manipular produtos
async function getProdutos() {
    return fetchAPI('/produtos');
}

async function cadastrarProduto(produto) {
    return fetchAPI('/produtos', {
        method: 'POST',
        body: JSON.stringify(produto)
    });
}

// Funções para manipular vendas
async function getVendas() {
    return fetchAPI('/vendas');
}

async function cadastrarVenda(venda) {
    return fetchAPI('/vendas', {
        method: 'POST',
        body: JSON.stringify(venda)
    });
}

// Funções de renderização
function renderProdutos(produtos) {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h2>Produtos</h2>
        <button id="novo-produto">Novo Produto</button>
        <div class="grid-container">
            ${produtos.map(produto => `
                <div class="card">
                    <h3>${produto.nome}</h3>
                    <p>Preço: R$ ${produto.preco.toFixed(2)}</p>
                    <p>Estoque: ${produto.quantidade}</p>
                </div>
            `).join('')}
        </div>
    `;
}

function renderVendas(vendas) {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h2>Vendas</h2>
        <button id="nova-venda">Nova Venda</button>
        <div class="grid-container">
            ${vendas.map(venda => `
                <div class="card">
                    <h3>Venda #${venda.id}</h3>
                    <p>Data: ${new Date(venda.data).toLocaleDateString()}</p>
                    <p>Total: R$ ${venda.total.toFixed(2)}</p>
                </div>
            `).join('')}
        </div>
    `;
}

// Event Listeners
document.getElementById('produtos-link').addEventListener('click', async (e) => {
    e.preventDefault();
    try {
        const produtos = await getProdutos();
        renderProdutos(produtos);
    } catch (error) {
        console.error('Erro ao carregar produtos:', error);
    }
});

document.getElementById('vendas-link').addEventListener('click', async (e) => {
    e.preventDefault();
    try {
        const vendas = await getVendas();
        renderVendas(vendas);
    } catch (error) {
        console.error('Erro ao carregar vendas:', error);
    }
});
