import unittest
from flask import current_app
from app import create_app,db
import os
from app.services.area_service import AreaService
from app.models.area import Area
from app.models.grupo import Grupo
from app import db

class GrupoTestCase(unittest.TestCase):
    
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
        
    def test_area_creation(self):
        area = self.__nuevaarea()
        self.assertIsNotNone(area)
        self.assertEqual(area.nombre, "Basica")
        self.assertIsNotNone(area.grupo)
        
    def test_crear_area(self):
        area = self.__nuevaarea()
        AreaService.crear_area(area)
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.id)
        self.assertGreaterEqual(area.id, 1)
        self.assertEqual(area.nombre, "Basica")

    def test_area_busqueda(self):
        area = self.__nuevaarea()
        AreaService.crear_area(area)    
        r=AreaService.buscar_por_id(area.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Basica")


    def test_buscar_area(self):
        area1 = self.__nuevaarea()
        area2 = self.__nuevaarea()
        AreaService.crear_area(area1)
        AreaService.crear_area(area2)
        area = AreaService.buscar_todos()
        self.assertIsNotNone(area)
        self.assertEqual(len(area), 2)

    def test_actualizar_area(self):
        area= self.__nuevaarea()
        AreaService.crear_area(area)
        area.nombre = "Especial"
        area_actualizada = AreaService.actualizar_area(area.id, area)
        self.assertEqual(area_actualizada.nombre, "Especial")

    def test_borrar_area(self):
        area = self.__nuevaarea()
        AreaService.crear_area(area)
        AreaService.borrar_por_id(area.id)
        resultado = AreaService.borrar_por_id(area.id)
        self.assertIsNone(resultado)

    def __nuevaarea(self):
        area = Area()
        grupo = Grupo(nombre = "Grupo 1")
        area.nombre = 'Basica'
        area.grupo = grupo
        return area