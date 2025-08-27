'''from dataclasses import dataclass
from app.models.facultad import Facultad
from app.models.cargo import Cargo
from app import db


@dataclass(init=False, repr=True, eq=True)
class Autoridad(db.Model):
    __tablename__ = 'autoridades'
    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(50),nullable=False)
    cargo: Cargo = db.relationship('Cargo',lazy=True)
    telefono: str = db.Column(db.String(20),nullable=False)
    email: str = db.Column(db.String(50), nullable=False)
'''
from dataclasses import dataclass
from app.models.facultad import Facultad
from app.models.cargo import Cargo
from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

@dataclass(init=False, repr=True, eq=True)
class Autoridad(db.Model):
    __tablename__ = 'autoridades'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    cargo: Cargo = relationship('Cargo', lazy=True)
    cargo_id: Mapped[int] = mapped_column(Integer, ForeignKey('cargos.id'), nullable=True)  # Agregando clave foránea
    cargo: Mapped["Cargo"] = relationship("Cargo", lazy=True)  # Relación ahora correctamente definida
    telefono: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
