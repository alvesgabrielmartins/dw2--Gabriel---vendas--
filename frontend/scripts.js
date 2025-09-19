// Configuração da API
const API_URL = 'http://localhost:8000/api';

// Estado da aplicação
let produtos = [];
let carrinho = [];
let cupomAplicado = null;
let filtrosAtivos = {
    busca: '',
    categoria: '',
    precoMin: null,
    precoMax: null,
    ordenacao: '',
    apenasEmEstoque: false
};

// Gerenciamento de Tema
function initTheme() {
    const theme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', theme);
    return theme;
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Atualizar aria-label do botão
    const themeButton = document.getElementById('theme-toggle');
    themeButton.setAttribute('aria-label', 
        `Alternar para tema ${newTheme === 'light' ? 'escuro' : 'claro'}`
    );
}

// Funções de utilidade
const formatarPreco = (preco) => {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(preco);
};

const calcularTotal = () => {
    const subtotal = carrinho.reduce((total, item) => total + (item.preco * item.quantidade), 0);
    const desconto = cupomAplicado === 'ALUNO10' ? subtotal * 0.1 : 0;
    return {
        subtotal,
        desconto,
        total: subtotal - desconto
    };
};

// Funções da API
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

async function getProdutos() {
    produtos = await fetchAPI('/produtos');
    renderizarProdutos();
}

async function cadastrarProduto(produto) {
    return fetchAPI('/produtos', {
        method: 'POST',
        body: JSON.stringify(produto)
    });
}

async function finalizarPedido(pedido) {
    return fetchAPI('/pedidos', {
        method: 'POST',
        body: JSON.stringify({
            ...pedido,
            cupom: cupomAplicado
        })
    });
}

// Funções de renderização
function renderizarProdutos() {
    const grid = document.querySelector('.produtos-grid');
    grid.innerHTML = produtos
        .map(produto => `
            <div class="produto-card" data-id="${produto.id}">
                <img src="${produto.imagem || 'https://via.placeholder.com/200'}" alt="${produto.nome}" class="produto-imagem">
                <div class="produto-info">
                    <h3 class="produto-nome">${produto.nome}</h3>
                    <p class="produto-preco">${formatarPreco(produto.preco)}</p>
                    <p class="produto-estoque">Estoque: ${produto.quantidade ?? produto.estoque ?? 0}</p>
                    <button 
                        onclick="adicionarAoCarrinho(${produto.id})"
                        class="btn-primary"
                        ${(produto.quantidade ?? produto.estoque) === 0 ? 'disabled' : ''}
                        aria-label="${(produto.quantidade ?? produto.estoque) === 0 ? 'Produto indisponível' : 'Adicionar ao carrinho'}"
                    >
                        ${(produto.quantidade ?? produto.estoque) === 0 ? 'Indisponível' : 'Adicionar ao Carrinho'}
                    </button>
                </div>
            </div>
        `)
        .join('');
}

function renderizarCarrinho() {
    const cartItems = document.querySelector('.cart-items');
    const totais = calcularTotal();
    
    cartItems.innerHTML = carrinho
        .map(item => `
            <div class="cart-item">
                <img src="${item.imagem || 'https://via.placeholder.com/50'}" alt="${item.nome}" width="50" height="50">
                <div class="cart-item-info">
                    <h4>${item.nome}</h4>
                    <p>${formatarPreco(item.preco)} x ${item.quantidade}</p>
                </div>
                <button 
                    onclick="removerDoCarrinho(${item.id})"
                    aria-label="Remover ${item.nome} do carrinho"
                >
                    &times;
                </button>
            </div>
        `)
        .join('');

    document.getElementById('subtotal').textContent = formatarPreco(totais.subtotal);
    document.getElementById('desconto').textContent = formatarPreco(totais.desconto);
    document.getElementById('total').textContent = formatarPreco(totais.total);
    
    // Atualizar badge do carrinho
    const badge = document.querySelector('.cart-badge');
    badge.textContent = carrinho.reduce((total, item) => total + item.quantidade, 0);
}

// Funções de manipulação do carrinho
window.adicionarAoCarrinho = function(produtoId) {
    const produto = produtos.find(p => p.id === produtoId);
    if (!produto || produto.quantidade === 0) return;

    const itemCarrinho = carrinho.find(item => item.id === produtoId);
    if (itemCarrinho) {
        if (itemCarrinho.quantidade < produto.quantidade) {
            itemCarrinho.quantidade++;
        }
    } else {
        carrinho.push({ ...produto, quantidade: 1 });
    }

    salvarCarrinho();
    renderizarCarrinho();
};

window.removerDoCarrinho = function(produtoId) {
    carrinho = carrinho.filter(item => item.id !== produtoId);
    salvarCarrinho();
    renderizarCarrinho();
};

// Persistência do carrinho
function salvarCarrinho() {
    localStorage.setItem('carrinho', JSON.stringify(carrinho));
}

function carregarCarrinho() {
    const carrinhoSalvo = localStorage.getItem('carrinho');
    if (carrinhoSalvo) {
        carrinho = JSON.parse(carrinhoSalvo);
        renderizarCarrinho();
    }
}

// Filtros avançados
function aplicarFiltros(produtos) {
    return produtos.filter(produto => {
        // Filtro de busca
        if (filtrosAtivos.busca && !produto.nome.toLowerCase().includes(filtrosAtivos.busca.toLowerCase())) {
            return false;
        }
        
        // Filtro de categoria
        if (filtrosAtivos.categoria && produto.categoria !== filtrosAtivos.categoria) {
            return false;
        }
        
        // Filtro de preço mínimo
        if (filtrosAtivos.precoMin && produto.preco < filtrosAtivos.precoMin) {
            return false;
        }
        
        // Filtro de preço máximo
        if (filtrosAtivos.precoMax && produto.preco > filtrosAtivos.precoMax) {
            return false;
        }
        
        // Filtro de estoque
        if (filtrosAtivos.apenasEmEstoque && produto.estoque === 0) {
            return false;
        }
        
        return true;
    }).sort((a, b) => {
        if (!filtrosAtivos.ordenacao) return 0;
        
        switch (filtrosAtivos.ordenacao) {
            case 'preco_asc':
                return a.preco - b.preco;
            case 'preco_desc':
                return b.preco - a.preco;
            case 'nome':
                return a.nome.localeCompare(b.nome);
            default:
                return 0;
        }
    });
}

function atualizarListaProdutos() {
    const produtosFiltrados = aplicarFiltros(produtos);
    renderizarProdutos(produtosFiltrados);
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    // Inicializar tema
    initTheme();
    
    // Carregar dados
    getProdutos();
    carregarCarrinho();

    // Navegação
    document.getElementById('catalogo-link').addEventListener('click', (e) => {
        e.preventDefault();
        document.getElementById('catalogo').classList.add('active');
        document.getElementById('admin').classList.remove('active');
        e.target.setAttribute('aria-current', 'page');
        document.getElementById('admin-link').removeAttribute('aria-current');
    });

    document.getElementById('admin-link').addEventListener('click', (e) => {
        e.preventDefault();
        document.getElementById('admin').classList.add('active');
        document.getElementById('catalogo').classList.remove('active');
        e.target.setAttribute('aria-current', 'page');
        document.getElementById('catalogo-link').removeAttribute('aria-current');
    });

    // Carrinho
    document.getElementById('cart-button').addEventListener('click', () => {
        const modal = document.getElementById('cart-modal');
        const button = document.getElementById('cart-button');
        const isOpen = modal.classList.toggle('active');
        button.setAttribute('aria-pressed', isOpen);
    });

    document.querySelector('.close-modal').addEventListener('click', () => {
        document.getElementById('cart-modal').classList.remove('active');
        document.getElementById('cart-button').setAttribute('aria-pressed', false);
    });

    // Cupom
    document.getElementById('aplicar-cupom').addEventListener('click', () => {
        const codigo = document.getElementById('cupom-input').value.toUpperCase();
        if (codigo === 'ALUNO10') {
            cupomAplicado = codigo;
            renderizarCarrinho();
            alert('Cupom aplicado com sucesso!');
        } else {
            alert('Cupom inválido!');
        }
    });

    // Finalizar compra
    document.getElementById('finalizar-compra').addEventListener('click', async () => {
        try {
            const totais = calcularTotal();
            await finalizarPedido({
                itens: carrinho,
                total_final: totais.total
            });
            
            carrinho = [];
            salvarCarrinho();
            renderizarCarrinho();
            document.getElementById('cart-modal').classList.remove('active');
            alert('Pedido finalizado com sucesso!');
        } catch (error) {
            alert('Erro ao finalizar pedido: ' + error.message);
        }
    });

    // Formulário de produto
    document.getElementById('produto-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        const produto = {
            nome: formData.get('nome'),
            descricao: formData.get('descricao'),
            preco: parseFloat(formData.get('preco')),
            quantidade: parseInt(formData.get('estoque')),
            categoria: formData.get('categoria'),
            sku: formData.get('sku')
        };

        try {
            await cadastrarProduto(produto);
            e.target.reset();
            getProdutos();
            alert('Produto cadastrado com sucesso!');
        } catch (error) {
            alert('Erro ao cadastrar produto: ' + error.message);
        }
    });

    // Tema
    document.getElementById('theme-toggle').addEventListener('click', toggleTheme);

    // Filtros
    const filterForm = document.getElementById('filter-form');
    const filterButton = document.getElementById('filter-button');
    const filterPanel = document.getElementById('filter-panel');
    
    filterButton.addEventListener('click', () => {
        const isExpanded = filterPanel.classList.toggle('active');
        filterButton.setAttribute('aria-expanded', isExpanded);
        filterPanel.setAttribute('aria-hidden', !isExpanded);
    });

    filterForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        filtrosAtivos = {
            busca: document.getElementById('search-input').value,
            categoria: document.getElementById('categoria-select').value,
            precoMin: document.getElementById('preco-min').value ? parseFloat(document.getElementById('preco-min').value) : null,
            precoMax: document.getElementById('preco-max').value ? parseFloat(document.getElementById('preco-max').value) : null,
            ordenacao: document.getElementById('sort-select').value,
            apenasEmEstoque: document.getElementById('em-estoque').checked
        };
        
        atualizarListaProdutos();
        filterPanel.classList.remove('active');
        filterButton.setAttribute('aria-expanded', 'false');
        filterPanel.setAttribute('aria-hidden', 'true');
    });

    document.getElementById('limpar-filtros').addEventListener('click', () => {
        filterForm.reset();
        filtrosAtivos = {
            busca: '',
            categoria: '',
            precoMin: null,
            precoMax: null,
            ordenacao: '',
            apenasEmEstoque: false
        };
        atualizarListaProdutos();
    });
});
