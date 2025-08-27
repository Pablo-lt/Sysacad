import unittest
from flask import current_app
from app import create_app
import os

from app.models.especialidad import Especialidad
from app.models.tipo_especialidad import TipoEspecialidad
from app.services.especialidad_service import EspecialidadService
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
        
    def test_especialidad_creation(self):
        especialidad = self.__nuevaespecialidad()
        self.assertIsNotNone(especialidad)
        self.assertEqual(especialidad.nombre, "Especialidad de prueba")
        self.assertEqual(especialidad.letra, "E")
        self.assertEqual(especialidad.observacion, "Especialidad de prueba")
        self.assertIsNotNone(especialidad.tipo_especialidad)
        
    def test_crear_especialidad(self):
        especialidad = self.__nuevaespecialidad()
        EspecialidadService.crear_especialidad(especialidad)
        self.assertIsNotNone(especialidad)
        self.assertIsNotNone(especialidad.id)
        self.assertGreaterEqual(especialidad.id, 1)
        self.assertEqual(especialidad.nombre, "Especialidad de prueba")

    def test_especialidad_busqueda(self):
        especialidad = self.__nuevaespecialidad()
        EspecialidadService.crear_especialidad(especialidad)    
        r=EspecialidadService.buscar_por_id(especialidad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Especialidad de prueba")
        self.assertEqual(r.letra, "E")


    def test_buscar_especialidad(self):
        especialidad1 = self.__nuevaespecialidad()
        especialidad2 = self.__nuevaespecialidad()
        EspecialidadService.crear_especialidad(especialidad1)
        EspecialidadService.crear_especialidad(especialidad2)
        especialidad = EspecialidadService.buscar_todos()
        self.assertIsNotNone(especialidad)
        self.assertEqual(len(especialidad), 2)

    def test_actualizar_especialidad(self):
        especialidad= self.__nuevaespecialidad()
        EspecialidadService.crear_especialidad(especialidad)
        especialidad.nombre = "Especialidad de prueba Actualizada"
        especialidad_actualizada = EspecialidadService.actualizar_especialidad(especialidad.id, especialidad)
        self.assertEqual(especialidad_actualizada.nombre, "Especialidad de prueba Actualizada")

    def test_borrar_especialidad(self):
        especialidad = self.__nuevaespecialidad()
        EspecialidadService.crear_especialidad(especialidad)
        EspecialidadService.borrar_por_id(especialidad.id)
        resultado = EspecialidadService.borrar_por_id(especialidad.id)
        self.assertIsNone(resultado)

    def __nuevaespecialidad(self):
        especialidad = Especialidad()
        tipo_especialidad = TipoEspecialidad(nombre = "Prueba",nivel = "1")
        especialidad.nombre = "Especialidad de prueba"
        especialidad.letra = "E"
        especialidad.observacion = "Especialidad de prueba"
        especialidad.tipo_especialidad = tipo_especialidad
        return especialidad
        