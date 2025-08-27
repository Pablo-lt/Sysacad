'''
from dataclasses import dataclass
from app.models.categoria_cargo import CategoriaCargo
from app.models.tipo_dedicacion import TipoDedicacion


@dataclass(init=False, repr=True, eq=True)
class Cargo:
    nombre: str
    puntos: int
    categoria_cargo: CategoriaCargo
    tipo_dedicacion: TipoDedicacion
'''

from dataclasses import dataclass
from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

@dataclass(init=False, repr=True, eq=True)
class Cargo(db.Model):  # Ahora Cargo hereda de db.Model
    __tablename__ = 'cargos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    puntos: Mapped[int] = mapped_column(Integer, nullable=False)

    categoria_cargo_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('categoria_cargos.id'), nullable=True)
    tipo_dedicacion_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('tipo_dedicaciones.id'), nullable=True)

'''
    categoria_cargo: CategoriaCargo = relationship("CategoriaCargo", backref="cargos")
    categoria_cargo_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('categoria_cargos.id'))
    categoria_cargo: Mapped[CategoriaCargo] = mapped_column(relationship("CategoriaCargo", backref="cargos"))
    tipo_dedicacion: TipoDedicacion = relationship("TipoDedicacion", backref="cargos")
    tipo_dedicacion_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('tipo_dedicaciones.id'))
    tipo_dedicacion: Mapped[TipoDedicacion] = mapped_column(relationship("TipoDedicacion", backref="cargos"))
'''