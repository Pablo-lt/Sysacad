import unittest
import os
from flask import current_app
from app import create_app
from app.models.autoridad import Autoridad
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo
from app.models.tipo_dedicacion import TipoDedicacion
from app.services.autoridad_service import AutoridadService
from app import db

class AutoridadTestCase(unittest.TestCase):
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
        
    def test_autoridad_creation(self):
        autoridad = self.__nuevaautoridad()
        self.assertIsNotNone(autoridad)
        self.assertEqual(autoridad.nombre, "Juan Perez")
        self.assertIsNotNone(autoridad.cargo)
        self.assertEqual(autoridad.cargo.nombre, "Decano")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "abc@gmail.com")
        self.assertIsNotNone(autoridad.cargo.categoria_cargo)
        self.assertEqual(autoridad.cargo.categoria_cargo.nombre, "Categoria 1")

    
    def test_crear_autoridad(self):
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear_autoridad(autoridad)
        self.assertIsNotNone(autoridad)
        self.assertIsNotNone(autoridad.id)
        self.assertGreaterEqual(autoridad.id, 1)
        self.assertEqual(autoridad.nombre, "Juan Perez")
        
    def test_autoridad_busqueda(self):
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear_autoridad(autoridad)
        r = AutoridadService.buscar_por_id(autoridad.id)
        self.assertIsNotNone(r)
        self.assertEqual(autoridad.nombre, "Juan Perez")
        self.assertEqual(autoridad.cargo.nombre, "Decano")
    
    def test_buscar_autoridades(self):
        autoridad1 = self.__nuevaautoridad()
        autoridad2 = self.__nuevaautoridad()
        AutoridadService.crear_autoridad(autoridad1)
        AutoridadService.crear_autoridad(autoridad2)
        autoridades = AutoridadService.buscar_todos()
        self.assertIsNotNone(autoridades)
        self.assertEqual(len(autoridades), 2)
        
    def test_actualizar_autoridad(self):
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear_autoridad(autoridad)
        autoridad.nombre = "Julian Pepito"
        autoridad_actualizada = AutoridadService.actualizar_autoridad(autoridad.id, autoridad)
        self.assertEqual(autoridad_actualizada.nombre, "Julian Pepito")
        
    def test_borrar_autoridad(self):
        autoridad = self.__nuevaautoridad()
        AutoridadService.crear_autoridad(autoridad)
        db.session.delete(autoridad)
        db.session.commit()
        autoridad_borrada = AutoridadService.borrar_por_id(autoridad.id)
        self.assertIsNone(autoridad_borrada)
    
    
    def __nuevaautoridad(self):
        autoridad = Autoridad()
        cargo = Cargo()
        tipo_dedicacion = TipoDedicacion()
        cargo.nombre= "Decano"
        cargo.puntos= 100
        cargo.categoria_cargo= CategoriaCargo()
        cargo.categoria_cargo.nombre= "Categoria 1"
        cargo.tipo_dedicacion = tipo_dedicacion
        cargo.tipo_dedicacion.nombre = "Simple"
        cargo.tipo_dedicacion.observacion = "Observacion 1"
        autoridad.nombre = "Juan Perez"
        autoridad.cargo= cargo
        autoridad.telefono= "123456789"
        autoridad.email= "abc@gmail.com"
        return autoridad
    

if __name__ == '__main__':
    unittest.main()
