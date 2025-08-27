# app/services/alumno_service.py
from app import db
from app.models import Alumno
from app.repositories.interfaces import Interface_Alumno_Repositorio
from typing import List, Optional
from app.exporters.interfaces import IAlumnoExporter
from typing import Optional

class AlumnoService:

    def __init__(self, repository: Interface_Alumno_Repositorio):
        self.repository = repository

    def crear_alumno(self, alumno: Alumno) -> Alumno:
        self.repository.crear(alumno)
        db.session.commit()  # commit aquí
        return alumno
    
    def buscar_por_id(self, id: int) -> Optional[Alumno]:
        return self.repository.buscar_por_id(id)
    
    def buscar_todos(self) -> List[Alumno]:
        return self.repository.buscar_todos()
    
    def actualizar_alumno(self, id: int, alumno: Alumno) -> Optional[Alumno]:
        alumno_existente = self.repository.buscar_por_id(id)
        if not alumno_existente:
            return None

        # lógica de negocio: copiar solo los campos permitidos
        alumno_existente.nombre = alumno.nombre
        alumno_existente.apellido = alumno.apellido
        alumno_existente.nro_legajo = alumno.nro_legajo
        alumno_existente.nro_documento = alumno.nro_documento
        alumno_existente.fecha_nacimiento = alumno.fecha_nacimiento
        alumno_existente.sexo = alumno.sexo
        alumno_existente.fecha_ingreso = alumno.fecha_ingreso

        actualizado = self.repository.actualizar(alumno_existente)
        db.session.commit()
        return actualizado
    
    def borrar_por_id(self, id: int) -> Optional[Alumno]:
        alumno = self.repository.borrar_por_id(id)
        if not alumno:
            return None
        db.session.commit()
        return alumno

    def ficha_alumno(self, nro_legajo: int, exporter: IAlumnoExporter) -> Optional[tuple]:
        alumno = self.repository.buscar_por_legajo(nro_legajo)
        if not alumno:
            return None
        return exporter.export(alumno), exporter.content_type()