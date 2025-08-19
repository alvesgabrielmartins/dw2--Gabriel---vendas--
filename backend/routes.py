from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from datetime import datetime
from models import Produto, Venda, ItemVenda
from main import SessionLocal

# Schemas Pydantic
class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        orm_mode = True

class ItemVendaBase(BaseModel):
    produto_id: int
    quantidade: int

class VendaCreate(BaseModel):
    itens: List[ItemVendaBase]

class VendaResponse(BaseModel):
    id: int
    data: datetime
    total: float
    itens: List[ItemVendaBase]

    class Config:
        orm_mode = True

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routers
router = APIRouter()

@router.get("/produtos", response_model=List[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()

@router.post("/produtos", response_model=ProdutoResponse)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    db_produto = Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@router.get("/vendas", response_model=List[VendaResponse])
def listar_vendas(db: Session = Depends(get_db)):
    return db.query(Venda).all()

@router.post("/vendas", response_model=VendaResponse)
def criar_venda(venda: VendaCreate, db: Session = Depends(get_db)):
    # Criar venda
    nova_venda = Venda(total=0)
    db.add(nova_venda)
    db.commit()
    
    total = 0
    # Adicionar itens
    for item in venda.itens:
        produto = db.query(Produto).filter(Produto.id == item.produto_id).first()
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        if produto.quantidade < item.quantidade:
            raise HTTPException(status_code=400, detail="Quantidade insuficiente em estoque")
        
        # Criar item de venda
        item_venda = ItemVenda(
            venda_id=nova_venda.id,
            produto_id=item.produto_id,
            quantidade=item.quantidade,
            preco_unitario=produto.preco
        )
        db.add(item_venda)
        
        # Atualizar estoque
        produto.quantidade -= item.quantidade
        total += produto.preco * item.quantidade
    
    # Atualizar total da venda
    nova_venda.total = total
    db.commit()
    db.refresh(nova_venda)
    return nova_venda
