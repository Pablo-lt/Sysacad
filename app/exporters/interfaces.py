# app/exporters/interfaces.py
from typing import Protocol
from app.models import Alumno

class IAlumnoExporter(Protocol):
    def export(self, alumno: Alumno) -> bytes | dict: ...
    def content_type(self) -> str: ...
