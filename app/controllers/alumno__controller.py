# app/controllers/alumno_controller.py
from flask import Blueprint, jsonify, Response, request
from app.repositories.Alumno_Repositorio import AlumnoRepository
from app.services.Alumno_service import AlumnoService
from app.exporters.alumno_json_exporter import AlumnoJsonExporter
from app.exporters.alumno_pdf_exporter import AlumnoPdfExporter

alumno_bp = Blueprint("alumno", __name__)
service = AlumnoService(AlumnoRepository())

@alumno_bp.route("/alumno/<int:legajo>/ficha")
def ficha_alumno(legajo):
    formato = request.args.get("formato", "json")

    if formato == "pdf":
        data, content_type = service.ficha_alumno(legajo, AlumnoPdfExporter())
        return Response(data, mimetype=content_type)
    else:
        data, content_type = service.ficha_alumno(legajo, AlumnoJsonExporter())
        return jsonify(data)
