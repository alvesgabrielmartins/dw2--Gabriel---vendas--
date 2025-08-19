from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from main import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(60), index=True)
    descricao = Column(Text, nullable=True)
    preco = Column(Float)
    quantidade = Column(Integer)
    categoria = Column(String(50))
    sku = Column(String(50), nullable=True)
    imagem = Column(String(255), nullable=True)

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, default=datetime.utcnow)
    cupom = Column(String(50), nullable=True)
    subtotal = Column(Float)
    desconto = Column(Float)
    total_final = Column(Float)
    itens = relationship("ItemPedido", back_populates="pedido")

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    preco_unitario = Column(Float)
    
    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto")
