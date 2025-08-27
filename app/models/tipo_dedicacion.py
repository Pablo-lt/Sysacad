'''from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class TipoDedicacion(db.Model):
    __tablename__ = 'tipo_dedicaciones'

    nombre: str = db.Column(db.String(100), primary_key=True)
    observacion: str = db.Column(db.String(500))
    '''
from dataclasses import dataclass
from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

@dataclass(init=False, repr=True, eq=True)
class TipoDedicacion(db.Model):
    __tablename__ = 'tipo_dedicaciones'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    observacion: Mapped[str] = mapped_column(String(100), nullable=True)
