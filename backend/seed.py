from database import engine, SessionLocal
from models import Base, Produto
import json

# Criar todas as tabelas
Base.metadata.create_all(bind=engine)

# Dados de exemplo para produtos
produtos = [
    {
        "nome": "Caderno Universitário 10 Matérias",
        "descricao": "Caderno com 200 folhas, capa dura",
        "preco": 25.90,
        "quantidade": 50,
        "categoria": "papelaria",
        "sku": "CAD-UNI-10M",
    },
    {
        "nome": "Mochila Escolar",
        "descricao": "Mochila resistente com múltiplos compartimentos",
        "preco": 89.90,
        "quantidade": 30,
        "categoria": "acessorios",
        "sku": "MCH-ESC-01",
    },
    {
        "nome": "Kit Lápis de Cor 24 Cores",
        "descricao": "Lápis de cor de alta qualidade",
        "preco": 35.50,
        "quantidade": 40,
        "categoria": "papelaria",
        "sku": "LAP-COR-24",
    },
    {
        "nome": "Uniforme Escolar - Camiseta",
        "descricao": "Camiseta polo em algodão",
        "preco": 45.00,
        "quantidade": 100,
        "categoria": "uniforme",
        "sku": "UNF-CAM-P",
    },
    {
        "nome": "Estojo Escolar",
        "descricao": "Estojo com 3 compartimentos",
        "preco": 18.90,
        "quantidade": 60,
        "categoria": "papelaria",
        "sku": "EST-3C-01",
    },
    {
        "nome": "Livro de Matemática",
        "descricao": "Livro didático do 9º ano",
        "preco": 129.90,
        "quantidade": 25,
        "categoria": "livros",
        "sku": "LIV-MAT-9",
    },
    {
        "nome": "Caneta Esferográfica Azul",
        "descricao": "Pacote com 10 unidades",
        "preco": 12.50,
        "quantidade": 80,
        "categoria": "papelaria",
        "sku": "CAN-AZ-10",
    },
    {
        "nome": "Régua 30cm",
        "descricao": "Régua transparente de acrílico",
        "preco": 4.90,
        "quantidade": 120,
        "categoria": "papelaria",
        "sku": "REG-30-01",
    },
    {
        "nome": "Apontador com Depósito",
        "descricao": "Apontador de metal com depósito",
        "preco": 8.90,
        "quantidade": 70,
        "categoria": "papelaria",
        "sku": "APT-DEP-01",
    },
    {
        "nome": "Borracha Branca",
        "descricao": "Borracha macia para lápis",
        "preco": 2.50,
        "quantidade": 150,
        "categoria": "papelaria",
        "sku": "BOR-BR-01",
    },
    {
        "nome": "Caderno de Desenho",
        "descricao": "Caderno espiral com 48 folhas",
        "preco": 15.90,
        "quantidade": 45,
        "categoria": "papelaria",
        "sku": "CAD-DES-01",
    },
    {
        "nome": "Cola Branca",
        "descricao": "Cola líquida 90g",
        "preco": 3.90,
        "quantidade": 100,
        "categoria": "papelaria",
        "sku": "COL-BR-90",
    },
    {
        "nome": "Agenda Escolar 2025",
        "descricao": "Agenda com planejamento semanal",
        "preco": 29.90,
        "quantidade": 40,
        "categoria": "papelaria",
        "sku": "AGD-2025",
    },
    {
        "nome": "Kit Compasso",
        "descricao": "Kit geométrico com compasso e transferidor",
        "preco": 15.90,
        "quantidade": 35,
        "categoria": "papelaria",
        "sku": "KIT-GEO-01",
    },
    {
        "nome": "Uniforme Escolar - Calça",
        "descricao": "Calça em tecido tactel",
        "preco": 65.00,
        "quantidade": 80,
        "categoria": "uniforme",
        "sku": "UNF-CAL-M",
    },
    {
        "nome": "Dicionário de Português",
        "descricao": "Dicionário completo da língua portuguesa",
        "preco": 89.90,
        "quantidade": 20,
        "categoria": "livros",
        "sku": "DIC-PORT",
    },
    {
        "nome": "Atlas Geográfico",
        "descricao": "Atlas mundial atualizado",
        "preco": 75.90,
        "quantidade": 15,
        "categoria": "livros",
        "sku": "ATL-GEO",
    },
    {
        "nome": "Pasta com Elástico",
        "descricao": "Pasta plástica tamanho A4",
        "preco": 7.90,
        "quantidade": 90,
        "categoria": "papelaria",
        "sku": "PST-A4-EL",
    },
    {
        "nome": "Calculadora Científica",
        "descricao": "Calculadora com funções científicas",
        "preco": 45.90,
        "quantidade": 25,
        "categoria": "acessorios",
        "sku": "CALC-CIE",
    },
    {
        "nome": "Uniforme Educação Física",
        "descricao": "Conjunto de short e camiseta",
        "preco": 55.00,
        "quantidade": 60,
        "categoria": "uniforme",
        "sku": "UNF-EDF",
    }
        "preco": 5.90,
        "quantidade": 90,
        "categoria": "papelaria",
        "sku": "COL-BR-90",
    },
    {
        "nome": "Tesoura Escolar",
        "descricao": "Tesoura sem ponta",
        "preco": 7.90,
        "quantidade": 55,
        "categoria": "papelaria",
        "sku": "TES-SP-01",
    },
    {
        "nome": "Uniforme Escolar - Calça",
        "descricao": "Calça em tactel",
        "preco": 65.00,
        "quantidade": 80,
        "categoria": "uniforme",
        "sku": "UNF-CAL-P",
    },
    {
        "nome": "Livro de Português",
        "descricao": "Livro didático do 9º ano",
        "preco": 129.90,
        "quantidade": 25,
        "categoria": "livros",
        "sku": "LIV-POR-9",
    },
    {
        "nome": "Agenda Escolar",
        "descricao": "Agenda anual capa dura",
        "preco": 28.90,
        "quantidade": 40,
        "categoria": "papelaria",
        "sku": "AGE-AN-01",
    },
    {
        "nome": "Kit Geométrico",
        "descricao": "Kit com régua, esquadros e transferidor",
        "preco": 22.90,
        "quantidade": 35,
        "categoria": "papelaria",
        "sku": "KIT-GEO-01",
    },
    {
        "nome": "Dicionário de Inglês",
        "descricao": "Dicionário Inglês-Português",
        "preco": 89.90,
        "quantidade": 20,
        "categoria": "livros",
        "sku": "DIC-ING-01",
    },
    {
        "nome": "Papel Sulfite A4",
        "descricao": "Pacote com 500 folhas",
        "preco": 32.90,
        "quantidade": 60,
        "categoria": "papelaria",
        "sku": "PAP-A4-500",
    },
    {
        "nome": "Lancheira Térmica",
        "descricao": "Lancheira com isolamento térmico",
        "preco": 49.90,
        "quantidade": 25,
        "categoria": "acessorios",
        "sku": "LAN-TER-01",
    }
]

def seed_database():
    db = SessionLocal()
    try:
        # Limpar tabelas
        db.query(Produto).delete()
        
        # Inserir produtos
        for produto_data in produtos:
            produto = Produto(**produto_data)
            db.add(produto)
        
        db.commit()
        print("Database seeded successfully!")
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
