from dataclasses import dataclass  
from app.models.tipo_especialidad import TipoEspecialidad
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from app import db

@dataclass(init=False, repr=True, eq=True)
class Especialidad(db.Model):
    __tablename__ = 'especialidades'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    letra: Mapped[str] = mapped_column(String(100), nullable=False)
    observacion: Mapped[str] = mapped_column(String(100), nullable=False)

    tipo_especialidad_id: Mapped[int] = mapped_column(ForeignKey("tipo_especialidades.id"), nullable=True)
    tipo_especialidad: Mapped["TipoEspecialidad"] = relationship("TipoEspecialidad", backref="especialidades")
