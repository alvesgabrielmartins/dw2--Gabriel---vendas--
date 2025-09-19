from database import engine, SessionLocal
from models import Base, Produto
import json

from database import engine, SessionLocal
from models import Base, Produto


# Criar todas as tabelas
Base.metadata.create_all(bind=engine)

# Dados de exemplo para produtos (lista reduzida e plausível)
produtos = [
    {"nome": "Caderno Universitário 10 Matérias", "descricao": "Caderno com 200 folhas, capa dura", "preco": 25.90, "quantidade": 50, "categoria": "papelaria", "sku": "CAD-UNI-10M"},
    {"nome": "Mochila Escolar", "descricao": "Mochila resistente com múltiplos compartimentos", "preco": 89.90, "quantidade": 30, "categoria": "acessorios", "sku": "MCH-ESC-01"},
    {"nome": "Kit Lápis de Cor 24 Cores", "descricao": "Lápis de cor de alta qualidade", "preco": 35.50, "quantidade": 40, "categoria": "papelaria", "sku": "LAP-COR-24"},
    {"nome": "Uniforme Escolar - Camiseta", "descricao": "Camiseta polo em algodão", "preco": 45.00, "quantidade": 100, "categoria": "uniforme", "sku": "UNF-CAM-P"},
    {"nome": "Estojo Escolar", "descricao": "Estojo com 3 compartimentos", "preco": 18.90, "quantidade": 60, "categoria": "papelaria", "sku": "EST-3C-01"},
    {"nome": "Livro de Matemática", "descricao": "Livro didático do 9º ano", "preco": 129.90, "quantidade": 25, "categoria": "livros", "sku": "LIV-MAT-9"},
    {"nome": "Caneta Esferográfica Azul (10)", "descricao": "Pacote com 10 unidades", "preco": 12.50, "quantidade": 80, "categoria": "papelaria", "sku": "CAN-AZ-10"},
    {"nome": "Régua 30cm", "descricao": "Régua transparente de acrílico", "preco": 4.90, "quantidade": 120, "categoria": "papelaria", "sku": "REG-30-01"},
    {"nome": "Apontador com Depósito", "descricao": "Apontador de metal com depósito", "preco": 8.90, "quantidade": 70, "categoria": "papelaria", "sku": "APT-DEP-01"},
    {"nome": "Borracha Branca", "descricao": "Borracha macia para lápis", "preco": 2.50, "quantidade": 150, "categoria": "papelaria", "sku": "BOR-BR-01"},
    {"nome": "Caderno de Desenho", "descricao": "Caderno espiral com 48 folhas", "preco": 15.90, "quantidade": 45, "categoria": "papelaria", "sku": "CAD-DES-01"},
    {"nome": "Cola Branca 90g", "descricao": "Cola líquida 90g", "preco": 3.90, "quantidade": 100, "categoria": "papelaria", "sku": "COL-BR-90"},
    {"nome": "Agenda Escolar 2025", "descricao": "Agenda com planejamento semanal", "preco": 29.90, "quantidade": 40, "categoria": "papelaria", "sku": "AGD-2025"},
    {"nome": "Kit Compasso", "descricao": "Kit geométrico com compasso e transferidor", "preco": 15.90, "quantidade": 35, "categoria": "papelaria", "sku": "KIT-GEO-01"},
    {"nome": "Uniforme Escolar - Calça", "descricao": "Calça em tecido tactel", "preco": 65.00, "quantidade": 80, "category": "uniforme", "sku": "UNF-CAL-M"},
    {"nome": "Dicionário de Português", "descricao": "Dicionário completo da língua portuguesa", "preco": 89.90, "quantidade": 20, "categoria": "livros", "sku": "DIC-PORT"},
    {"nome": "Atlas Geográfico", "descricao": "Atlas mundial atualizado", "preco": 75.90, "quantidade": 15, "categoria": "livros", "sku": "ATL-GEO"},
    {"nome": "Pasta com Elástico A4", "descricao": "Pasta plástica tamanho A4", "preco": 7.90, "quantidade": 90, "categoria": "papelaria", "sku": "PST-A4-EL"},
    {"nome": "Calculadora Científica", "descricao": "Calculadora com funções científicas", "preco": 45.90, "quantidade": 25, "categoria": "acessorios", "sku": "CALC-CIE"},
    {"nome": "Lancheira Térmica", "descricao": "Lancheira com isolamento térmico", "preco": 49.90, "quantidade": 25, "categoria": "acessorios", "sku": "LAN-TER-01"}
]


def seed_database():
    db = SessionLocal()
    try:
        # Limpar tabela de produtos
        db.query(Produto).delete()

        # Inserir produtos
        for produto_data in produtos:
            # corrigir chaves erradas se houver
            produto_data = {k: v for k, v in produto_data.items()}
            # mapear 'category' para 'categoria' se presente
            if 'category' in produto_data and 'categoria' not in produto_data:
                produto_data['categoria'] = produto_data.pop('category')
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
