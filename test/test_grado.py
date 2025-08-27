import unittest
from flask import current_app
from app import create_app,db
from app.models.grado import Grado
from app.services.grado_service import GradoService
import os


class GradoTestCase(unittest.TestCase):
    
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
        
    def test_grado_creation(self):
        grado = self.__nuevogrado()
        self.assertIsNotNone(grado)
        self.assertEqual(grado.nombre,"3ro")


    def test_crear_grado(self):
        grado = self.__nuevogrado()
        GradoService.crear_grado(grado)
        self.assertIsNotNone(grado)
        self.assertIsNotNone(grado.id)
        self.assertGreaterEqual(grado.id, 1)
        self.assertEqual(grado.nombre, "3ro")

    def test_grado_busqueda(self):
        grado = self.__nuevogrado()
        GradoService.crear_grado(grado)    
        r=GradoService.buscar_por_id(grado.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "3ro")


    def test_buscar_grado(self):
        grado1 = self.__nuevogrado()
        grado2 = self.__nuevogrado()
        GradoService.crear_grado(grado1)
        GradoService.crear_grado(grado2)
        grado = GradoService.buscar_todos()
        self.assertIsNotNone(grado)
        self.assertEqual(len(grado), 2)

    def test_actualizar_grado(self):
        grado= self.__nuevogrado()
        GradoService.crear_grado(grado)
        grado.nombre = "4to"
        grado_actualizada = GradoService.actualizar_grado(grado.id, grado)
        self.assertEqual(grado_actualizada.nombre, "4to")

    def test_borrar_grado(self):
        grado = self.__nuevogrado()
        GradoService.crear_grado(grado)
        GradoService.borrar_por_id(grado.id)
        resultado = GradoService.borrar_por_id(grado.id)
        self.assertIsNone(resultado)

    def __nuevogrado(self):
        grado=Grado()
        grado.nombre = "3ro"
        return grado
        
if __name__ == '__main__':
    unittest.main()