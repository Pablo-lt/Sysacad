from dataclasses import dataclass  
from app.models.orientacion import Orientacion
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from app import db

@dataclass(init=False, repr=True, eq=True)
class Departamento(db.Model):
    __tablename__ = 'departamentos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)

    orientacion_id: Mapped[int] = mapped_column(ForeignKey("orientaciones.id"), nullable=True)
    orientacion: Mapped["Orientacion"] = relationship("Orientacion", backref="departamentos")
