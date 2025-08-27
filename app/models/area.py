from dataclasses import dataclass
from app.models.grupo import Grupo  
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from app import db

@dataclass(init=False, repr=True, eq=True)
class Area(db.Model):
    __tablename__ = 'areas'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)

    grupo_id: Mapped[int] = mapped_column(ForeignKey("grupos.id"), nullable=False)
    grupo: Mapped["Grupo"] = relationship("Grupo", backref="areas")
