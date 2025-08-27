from dataclasses import dataclass
from sqlalchemy import DateTime  
from app import db

@dataclass(init=False, repr=True, eq=True)
class Plan(db.Model):
    __tablename__ = 'planes'
    
    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable= False)
    fecha_inicio: DateTime = db.Column(db.DateTime, nullable= False)
    fecha_fin: DateTime = db.Column(db.DateTime, nullable= False)
    observacion: str = db.Column(db.String(500), nullable= False)