from pathlib import Path

from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

CAMINHO_BANCO = Path(__file__).resolve().parent.parent / "spec" / "hashtag_sqlalchemy.db"

Base = declarative_base()

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)

    produtos = relationship("Produto", back_populates="categoria")

    def __repr__(self):
        return f"Categoria(id={self.id}, nome={self.nome!r})"


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)
    quantidade_estoque = Column(Integer, nullable=False, default=0)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    categoria = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        return f"Produto(id={self.id}, nome={self.nome!r}, preco={self.preco})"


def criar_engine(caminho_banco=CAMINHO_BANCO):
    engine = create_engine(f"sqlite:///{caminho_banco}")
    Base.metadata.create_all(engine)
    return engine


def nova_sessao(engine):
    Sessao = sessionmaker(bind=engine)
    return Sessao()