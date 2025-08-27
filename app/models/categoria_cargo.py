'''from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class CategoriaCargo(db.Model):
    __tablename__ = 'categoria_cargos'
    
    nombre: str = db.Column(db.String(100), primary_key=True)
    '''
from dataclasses import dataclass
from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

@dataclass(init=False, repr=True, eq=True)
class CategoriaCargo(db.Model):
    __tablename__ = 'categoria_cargos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
