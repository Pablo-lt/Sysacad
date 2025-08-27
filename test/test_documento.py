import unittest
from flask import current_app
from app import create_app
import os
from app.models.documento import Documento
from app.services.documento_service import DocumentoService
from app import db

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_documento_creation(self):
        documento = self.__nuevodocumento()
        self.assertIsNotNone(documento)
        self.assertEqual(documento.tipo_documento, "DNI")
        
    def test_crear_documento(self):
        documento = self.__nuevodocumento()
        DocumentoService.crear_documento(documento)
        self.assertIsNotNone(documento)
        self.assertIsNotNone(documento.id)
        self.assertGreaterEqual(documento.id, 1)
        self.assertEqual(documento.tipo_documento, "DNI")

    def test_documento_busqueda(self):
        documento = self.__nuevodocumento()
        DocumentoService.crear_documento(documento)    
        r=DocumentoService.buscar_por_id(documento.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.tipo_documento, "DNI")


    def test_buscar_documento(self):
        documento1 = self.__nuevodocumento()
        documento2 = self.__nuevodocumento()
        DocumentoService.crear_documento(documento1)
        DocumentoService.crear_documento(documento2)
        documento = DocumentoService.buscar_todos()
        self.assertIsNotNone(documento)
        self.assertEqual(len(documento), 2)

    def test_actualizar_documento(self):
        documento= self.__nuevodocumento()
        DocumentoService.crear_documento(documento)
        documento.tipo_documento = "Pasaporte"
        documento_actualizada = DocumentoService.actualizar_documento(documento.id, documento)
        self.assertEqual(documento_actualizada.tipo_documento, "Pasaporte")

    def test_borrar_documento(self):
        documento = self.__nuevodocumento()
        DocumentoService.crear_documento(documento)
        DocumentoService.borrar_por_id(documento.id)
        resultado = DocumentoService.borrar_por_id(documento.id)
        self.assertIsNone(resultado)
        
    def __nuevodocumento(self):
        documento = Documento()
        documento.tipo_documento = 'DNI'
        return documento
        
if __name__ == '__main__':
    unittest.main()