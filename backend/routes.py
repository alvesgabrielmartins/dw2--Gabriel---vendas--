from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel, constr, confloat, conint
from datetime import datetime
from models import Produto, Pedido, ItemPedido
from main import SessionLocal

# Schemas Pydantic
class ProdutoBase(BaseModel):
    nome: constr(min_length=3, max_length=60)
    descricao: Optional[str] = None
    preco: confloat(gt=0)
    quantidade: conint(ge=0)
    categoria: str
    sku: Optional[str] = None
    imagem: Optional[str] = None

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        orm_mode = True

class ItemPedidoBase(BaseModel):
    produto_id: int
    quantidade: conint(gt=0)

class ItemPedidoResponse(ItemPedidoBase):
    preco_unitario: float

    class Config:
        orm_mode = True

class PedidoCreate(BaseModel):
    itens: List[ItemPedidoBase]
    cupom: Optional[str] = None

class PedidoResponse(BaseModel):
    id: int
    data: datetime
    cupom: Optional[str]
    subtotal: float
    desconto: float
    total_final: float
    itens: List[ItemPedidoResponse]

    class Config:
        orm_mode = True

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Funções auxiliares
def aplicar_cupom(subtotal: float, cupom: Optional[str]) -> float:
    if cupom == "ALUNO10":
        return subtotal * 0.1
    return 0

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

@router.get("/pedidos", response_model=List[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(Pedido).all()

@router.post("/pedidos", response_model=PedidoResponse)
def criar_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    # Calcular valores
    subtotal = 0
    itens_pedido = []
    
    # Verificar e processar itens
    for item in pedido.itens:
        produto = db.query(Produto).filter(Produto.id == item.produto_id).first()
        if not produto:
            raise HTTPException(status_code=404, detail=f"Produto {item.produto_id} não encontrado")
        if produto.quantidade < item.quantidade:
            raise HTTPException(status_code=400, detail=f"Quantidade insuficiente do produto {produto.nome}")
            
        subtotal += produto.preco * item.quantidade
        
        # Criar item do pedido
        item_pedido = ItemPedido(
            produto_id=item.produto_id,
            quantidade=item.quantidade,
            preco_unitario=produto.preco
        )
        itens_pedido.append(item_pedido)
        
        # Atualizar estoque
        produto.quantidade -= item.quantidade
    
    # Calcular desconto do cupom
    desconto = aplicar_cupom(subtotal, pedido.cupom)
    total_final = subtotal - desconto
    
    # Criar pedido
    novo_pedido = Pedido(
        cupom=pedido.cupom,
        subtotal=subtotal,
        desconto=desconto,
        total_final=total_final,
        itens=itens_pedido
    )
    
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido
