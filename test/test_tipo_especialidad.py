import unittest
from flask import current_app
from app import create_app
import os

from app.models.tipo_especialidad import TipoEspecialidad
from app.services.tipoespecialidad_service import TipoEspecialidadService
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
        
    def test_tipoespecialidad_creation(self):
        tipo_especialidad = self.__nuevo_tipoespecialidad()
        self.assertIsNotNone(tipo_especialidad)
        self.assertEqual(tipo_especialidad.nombre, 'Prueba')
        self.assertEqual(tipo_especialidad.nivel, '1')
        
    def test_crear_tipo_especialidad(self):
        tipo_especialidad = self.__nuevo_tipoespecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad)
        self.assertIsNotNone(tipo_especialidad.id)
        self.assertGreaterEqual(tipo_especialidad.id, 1)
        self.assertEqual(tipo_especialidad.nombre, "Prueba")
        self.assertEqual(tipo_especialidad.nivel, '1')

    def test_tipo_especialidad_busqueda(self):
        tipo_especialidad = self.__nuevo_tipoespecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)    
        r=TipoEspecialidadService.buscar_por_id(tipo_especialidad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Prueba")
        self.assertEqual(r.nivel, "1")


    def test_buscar_tipo_especialidad(self):
        tipo_especialidad1 = self.__nuevo_tipoespecialidad()
        tipo_especialidad2 = self.__nuevo_tipoespecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad1)
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad2)
        tipo_especialidad = TipoEspecialidadService.buscar_todos()
        self.assertIsNotNone(tipo_especialidad)
        self.assertEqual(len(tipo_especialidad), 2)

    def test_actualizar_tipo_especialidad(self):
        tipo_especialidad= self.__nuevo_tipoespecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
        tipo_especialidad.nombre = "Prueba actualizada"
        tipo_especialidad_actualizada = TipoEspecialidadService.actualizar_tipo_especialidad(tipo_especialidad.id, tipo_especialidad)
        self.assertEqual(tipo_especialidad_actualizada.nombre, "Prueba actualizada")

    def test_borrar_tipo_especialidad(self):
        tipo_especialidad = self.__nuevo_tipoespecialidad()
        TipoEspecialidadService.crear_tipo_especialidad(tipo_especialidad)
        TipoEspecialidadService.borrar_por_id(tipo_especialidad.id)
        resultado = TipoEspecialidadService.borrar_por_id(tipo_especialidad.id)
        self.assertIsNone(resultado)

    def __nuevo_tipoespecialidad(self):
        tipo_especialidad = TipoEspecialidad()
        tipo_especialidad.nombre = 'Prueba'
        tipo_especialidad.nivel = '1'
        return tipo_especialidad
        