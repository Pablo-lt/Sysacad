import unittest
from flask import current_app
from app import create_app
import os
from app.models.departamento import Departamento
from app.services.departamento_service import DepartamentoService
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
        
    def test_departamento_creation(self):
        departamento = self.__nuevodepartamento()
        self.assertIsNotNone(departamento)
        self.assertEqual(departamento.nombre, "Departamento 1")
        
    def test_crear_departamento(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear_departamento(departamento)
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.id)
        self.assertGreaterEqual(departamento.id, 1)
        self.assertEqual(departamento.nombre, "Departamento 1")

    def test_departamento_busqueda(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear_departamento(departamento)    
        r=DepartamentoService.buscar_por_id(departamento.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Departamento 1")

    def test_buscar_departamento(self):
        departamento1 = self.__nuevodepartamento()
        departamento2 = self.__nuevodepartamento()
        DepartamentoService.crear_departamento(departamento1)
        DepartamentoService.crear_departamento(departamento2)
        departamento = DepartamentoService.buscar_todos()
        self.assertIsNotNone(departamento)
        self.assertEqual(len(departamento), 2)

    def test_actualizar_departamento(self):
        departamento= self.__nuevodepartamento()
        DepartamentoService.crear_departamento(departamento)
        departamento.nombre = "Departamento 1"
        departamento_actualizada = DepartamentoService.actualizar_departamento(departamento.id, departamento)
        self.assertEqual(departamento_actualizada.nombre, "Departamento 1")

    def test_borrar_departamento(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear_departamento(departamento)
        DepartamentoService.borrar_por_id(departamento.id)
        resultado = DepartamentoService.borrar_por_id(departamento.id)
        self.assertIsNone(resultado)
        
    def __nuevodepartamento(self):
        departamento = Departamento()
        departamento.nombre = 'Departamento 1'
        return departamento
        
if __name__ == '__main__':
    unittest.main()