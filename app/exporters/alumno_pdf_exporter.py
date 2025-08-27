# app/exporters/alumno_pdf_exporter.py
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from app.models import Alumno
from app.exporters.interfaces import IAlumnoExporter

class AlumnoPdfExporter(IAlumnoExporter):
    def export(self, alumno: Alumno) -> bytes:
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)

        p.drawString(100, 800, f"Ficha del Alumno")
        p.drawString(100, 770, f"Legajo: {alumno.nro_legajo}")
        p.drawString(100, 750, f"Apellido: {alumno.apellido}")
        p.drawString(100, 730, f"Nombre: {alumno.nombre}")
        if alumno.facultad:
            p.drawString(100, 710, f"Facultad: {alumno.facultad.nombre}")

        p.showPage()
        p.save()
        buffer.seek(0)
        return buffer.read()

    def content_type(self) -> str:
        return "application/pdf"
