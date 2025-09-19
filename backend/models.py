from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(60), index=True, nullable=False)
    descricao = Column(Text, nullable=True)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, default=0)
    categoria = Column(String(50), nullable=True)
    sku = Column(String(50), nullable=True)

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, default=datetime.utcnow)
    cupom = Column(String(20), nullable=True)
    subtotal = Column(Float, default=0.0)
    desconto = Column(Float, default=0.0)
    total_final = Column(Float, default=0.0)

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'))
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)

    pedido = relationship('Pedido', backref='itens')
    produto = relationship('Produto')
