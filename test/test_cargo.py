import unittest
import os
from flask import current_app
from app import create_app
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo
from app.services.cargo_service import CargoService
from app import db

class CargoTestCase(unittest.TestCase):
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
        cargo = self.__nuevocargo()
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.categoria_cargo)
        self.assertEqual(cargo.categoria_cargo.nombre, "Categoria 1")
        self.assertEqual(cargo.nombre, "Decano")
        self.assertEqual(cargo.puntos, 100)
        
    def test_crear_cargo(self):
        cargo = self.__nuevocargo()
        CargoService.crear_cargo(cargo)
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.id)
        self.assertGreaterEqual(cargo.id, 1)
        self.assertEqual(cargo.nombre, "Decano")

    def test_cargo_busqueda(self):
        cargo = self.__nuevocargo()
        CargoService.crear_cargo(cargo)    
        r=CargoService.buscar_por_id(cargo.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Decano")
        self.assertEqual(r.categoria_cargo.nombre, "Categoria 1")


    def test_buscar_cargos(self):
        cargo1 = self.__nuevocargo()
        cargo2 = self.__nuevocargo()
        CargoService.crear_cargo(cargo1)
        CargoService.crear_cargo(cargo2)
        cargos = CargoService.buscar_todos()
        self.assertIsNotNone(cargos)
        self.assertEqual(len(cargos), 2)

    def test_actualizar_cargo(self):
        cargo= self.__nuevocargo()
        CargoService.crear_cargo(cargo)
        cargo.nombre = "Maestro"
        cargo_actualizado = CargoService.actualizar_cargo(cargo.id, cargo)
        self.assertEqual(cargo_actualizado.nombre, "Maestro")

    def test_borrar_cargo(self):
        cargo = self.__nuevocargo()
        CargoService.crear_cargo(cargo)
        CargoService.borrar_por_id(cargo.id)
        resultado = CargoService.buscar_por_id(cargo.id)
        self.assertIsNone(resultado)

    def __nuevocargo(self):
        cargo = Cargo()
        cargo.categoria_cargo= CategoriaCargo()
        cargo.categoria_cargo.nombre= "Categoria 1"
        cargo.nombre= "Decano"
        cargo.puntos= 100
        return cargo
        
if __name__ == '__main__':
    unittest.main()








