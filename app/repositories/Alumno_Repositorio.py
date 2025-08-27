# app/repositories/alumno_repository.py
from app import db
from app.models import Alumno
from app.repositories.interfaces import Interface_Alumno_Repositorio
from typing import List, Optional

class AlumnoRepository(Interface_Alumno_Repositorio):
    """
    Implementación concreta de un repositorio para Alumno.
    Encargado SOLO de acceder a la base de datos (sin commits).
    """

    def crear(self, alumno: Alumno) -> None:
        db.session.add(alumno)

    def buscar_por_id(self, id: int) -> Optional[Alumno]:
        return db.session.query(Alumno).filter_by(id=id).first()

    def buscar_todos(self) -> List[Alumno]:
        return db.session.query(Alumno).all()
    
    def actualizar(self, alumno: Alumno) -> Alumno:
        return db.session.merge(alumno)
    
    def borrar_por_id(self, id: int) -> Optional[Alumno]:
        alumno = db.session.query(Alumno).filter_by(id=id).first()
        if not alumno:
            return None
        db.session.delete(alumno)
        return alumno
