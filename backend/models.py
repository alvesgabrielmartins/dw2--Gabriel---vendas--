from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(60), index=True)
    descricao = Column(Text, nullable=True)
    preco = Column(Float)
    estoque = Column(Integer)
    categoria = Column(String(50))
    sku = Column(String(50), nullable=True)

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, default=datetime.utcnow)
    total_final = Column(Float)
    cupom_aplicado = Column(String(20), nullable=True)
