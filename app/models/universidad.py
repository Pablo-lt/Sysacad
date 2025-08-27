'''from dataclasses import dataclass  
from app import db
from app.models.facultad import Facultad

@dataclass(init=False, repr=True, eq=True)
class Univesrsidad(db.Model):
    __tablename__ = 'universidades'
    
    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable= False)
    sigla: str = db.Column(db.String(5), nullable= False)

    facultad_id = db.Column(db.Integer, db.ForeignKey('facultades.id'), nullable=True)
    facultad = db.relationship('Facultad', backref='universidades')'''
    
from dataclasses import dataclass  
from app import db
from app.models.facultad import Facultad
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

@dataclass(init=False, repr=True, eq=True)
class Universidad(db.Model):  # corregido el nombre de la clase
    __tablename__ = 'universidades'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    sigla: Mapped[str] = mapped_column(String(5), nullable=False)

    facultad_id: Mapped[int] = mapped_column(ForeignKey('facultades.id'), nullable=True)
    facultad: Mapped["Facultad"] = relationship('Facultad', backref='universidades')
