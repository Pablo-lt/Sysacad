import unittest
from flask import current_app
from app import create_app
import os
from app.models.especialidad import Especialidad
from app.models.materia import Materia
from app.models.orientacion import Orientacion
from app.services.orientacion_service import OrientacionService
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
        orientacion = self.__nuevaorientacion()
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.materia)
        self.assertIsNotNone(orientacion.especialidad)
        self.assertEqual(orientacion.nombre, "Orientacion 1")
        
    def test_crear_orientacion(self):
        orientacion = self.__nuevaorientacion()
        OrientacionService.crear_orientacion(orientacion)
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.id)
        self.assertGreaterEqual(orientacion.id, 1)
        self.assertEqual(orientacion.nombre, "Orientacion 1")

    def test_orientacion_busqueda(self):
        orientacion = self.__nuevaorientacion()
        OrientacionService.crear_orientacion(orientacion)    
        r=OrientacionService.buscar_por_id(orientacion.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Orientacion 1")

    def test_buscar_orientacion(self):
        orientacion1 = self.__nuevaorientacion()
        orientacion2 = self.__nuevaorientacion()
        OrientacionService.crear_orientacion(orientacion1)
        OrientacionService.crear_orientacion(orientacion2)
        orientacion = OrientacionService.buscar_todos()
        self.assertIsNotNone(orientacion)
        self.assertEqual(len(orientacion), 2)

    def test_actualizar_orientacion(self):
        orientacion= self.__nuevaorientacion()
        OrientacionService.crear_orientacion(orientacion)
        orientacion.nombre = "Orientacion 2"
        orientacion_actualizada = OrientacionService.actualizar_orientacion(orientacion.id, orientacion)
        self.assertEqual(orientacion_actualizada.nombre, "Orientacion 2")

    def test_borrar_orientacion(self):
        orientacion = self.__nuevaorientacion()
        OrientacionService.crear_orientacion(orientacion)
        OrientacionService.borrar_por_id(orientacion.id)
        resultado = OrientacionService.borrar_por_id(orientacion.id)
        self.assertIsNone(resultado)

    def __nuevaorientacion(self):
        orientacion= Orientacion()
        materia = Materia(nombre = "Matematicas",codigo = "MAT-101",observacion = "Esta es una materia de matematicas")
        especialidad = Especialidad(nombre = "Especialidad de prueba",letra = "E",observacion = "Especialidad de prueba")
        orientacion.materia = materia
        orientacion.especialidad = especialidad
        orientacion.nombre = 'Orientacion 1'
        return orientacion
        
if __name__ == '__main__':
    unittest.main()