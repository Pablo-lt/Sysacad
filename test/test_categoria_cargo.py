import unittest
import os
from flask import current_app
from app import create_app
from app.models.categoria_cargo import CategoriaCargo
from app.services.categoriacargo_service import CategoriaCargoService
from app import db

class CategoriaCargoTestCase(unittest.TestCase):
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
        
    def test_categoriacargo_creation(self):
        categoria_cargo = self.__nuevo_categoriacargo()
        self.assertIsNotNone(categoria_cargo)
        self.assertEqual(categoria_cargo.nombre, "Categoria 1")
        
    
    def test_crear_facultad(self):
        categoria_cargo = self.__nuevo_categoriacargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo)
        self.assertIsNotNone(categoria_cargo)
        self.assertIsNotNone(categoria_cargo.id)
        self.assertGreaterEqual(categoria_cargo.id, 1)
        self.assertEqual(categoria_cargo.nombre, "Categoria 1")

    def test_facultad_busqueda(self):
        categoria_cargo = self.__nuevo_categoriacargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo)    
        r=CategoriaCargoService.buscar_por_id(categoria_cargo.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Categoria 1")


    def test_buscar_facultades(self):
        categoria_cargo1 = self.__nuevo_categoriacargo()
        categoria_cargo2 = self.__nuevo_categoriacargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo1)
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo2)
        categoria_cargo = CategoriaCargoService.buscar_todos()
        self.assertIsNotNone(categoria_cargo)
        self.assertEqual(len(categoria_cargo), 2)

    def test_actualizar_facultad(self):
        categoria_cargo= self.__nuevo_categoriacargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo)
        categoria_cargo.nombre = "Categoria 1"
        categoria_cargo_actualizada = CategoriaCargoService.actualizar_categoria_cargo(categoria_cargo.id, categoria_cargo)
        self.assertEqual(categoria_cargo_actualizada.nombre, "Categoria 1")

    def test_borrar_facultad(self):
        categoria_cargo = self.__nuevo_categoriacargo()
        CategoriaCargoService.crear_categoria_cargo(categoria_cargo)
        CategoriaCargoService.borrar_por_id(categoria_cargo.id)
        resultado = CategoriaCargoService.buscar_por_id(categoria_cargo.id)
        self.assertIsNone(resultado)

    def __nuevo_categoriacargo(self):
        categoria_cargo = CategoriaCargo()
        categoria_cargo.nombre= "Categoria 1"
        return categoria_cargo
        
if __name__ == '__main__':
    unittest.main()