# app/exporters/alumno_json_exporter.py
from app.models import Alumno
from app.exporters.interfaces import IAlumnoExporter

class AlumnoJsonExporter(IAlumnoExporter):
    def export(self, alumno: Alumno) -> dict:
        return {
            "nro_legajo": alumno.nro_legajo,
            "apellido": alumno.apellido,
            "nombre": alumno.nombre,
            "facultad": alumno.facultad.nombre if alumno.facultad else None
        }

    def content_type(self) -> str:
        return "application/json"
