import unittest
import os
from flask import current_app
from app import create_app
from app.models.universidad import Universidad
from app.models.facultad import Facultad
from app.services.universidad_service import UniversidadService
from app import db

class UniversidadTestCase(unittest.TestCase):
    
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
    
    def test_universidad_creation(self):
        universidad = self.__nuevauniversidad()
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.nombre)
        self.assertEqual(universidad.nombre, "Universidad Tecnologica Nacional")
        self.assertEqual(universidad.sigla, "UTN")
        
    def test_crear_universidad(self):
        universidad = self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad)
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad.id, 1)
        self.assertEqual(universidad.nombre, "Universidad Tecnologica Nacional")

    def test_universidad_busqueda(self):
        universidad = self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad)    
        r=UniversidadService.buscar_por_id(universidad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Universidad Tecnologica Nacional")
        self.assertEqual(r.sigla, "UTN")


    def test_buscar_universidad(self):
        universidad1 = self.__nuevauniversidad()
        universidad2 = self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad1)
        UniversidadService.crear_universidad(universidad2)
        universidad = UniversidadService.buscar_todos()
        self.assertIsNotNone(universidad)
        self.assertEqual(len(universidad), 2)

    def test_actualizar_universidad(self):
        universidad= self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad)
        universidad.nombre = "Universidad Nacional de CUYO"
        universidad_actualizada = UniversidadService.actualizar_universidad(universidad.id, universidad)
        self.assertEqual(universidad_actualizada.nombre, "Universidad Nacional de CUYO")

    def test_borrar_universidad(self):
        universidad = self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad)
        UniversidadService.borrar_por_id(universidad.id)
        resultado = UniversidadService.borrar_por_id(universidad.id)
        self.assertIsNone(resultado)
        
    def __nuevauniversidad(self):
        facultad = Facultad(nombre = "Facultad de Ciencias",abreviatura = "FCC",
        directorio = "/facultad/ciencias",sigla = "FC",codigo_postal = "12345",ciudad = "Ciudad",domicilio = "Calle 123",telefono = "123456789",contacto = "Juan Perez",email = "1234@gmail.com")
        universidad = Universidad()
        universidad.facultad = facultad
        universidad.nombre = "Universidad Tecnologica Nacional"
        universidad.sigla = "UTN"
        return universidad
        
if __name__ == '__main__':
    unittest.main()