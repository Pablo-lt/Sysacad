import unittest
from flask import current_app
from app import create_app
import os
from app.services.materia_service import MateriaService
from app.models.materia import Materia
from app.models.nota import Nota
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
        
    def test_materia_creation(self):
        materia = self.__nuevamateria()
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, "Matematicas")
        self.assertEqual(materia.codigo, "MAT-101")
        self.assertEqual(materia.observacion, "Esta es una materia de matematicas")
        self.assertIsNotNone(materia.nota)
        
    def test_crear_materia(self):
        materia = self.__nuevamateria()
        MateriaService.crear_materia(materia)
        self.assertIsNotNone(materia)
        self.assertIsNotNone(materia.id)
        self.assertGreaterEqual(materia.id, 1)
        self.assertEqual(materia.nombre, "Matematicas")

    def test_materia_busqueda(self):
        materia = self.__nuevamateria()
        MateriaService.crear_materia(materia)    
        r=MateriaService.buscar_por_id(materia.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Matematicas")
        self.assertEqual(r.codigo, "MAT-101")
        self.assertEqual(r.observacion, "Esta es una materia de matematicas")


    def test_buscar_materia(self):
        materia1 = self.__nuevamateria()
        materia2 = self.__nuevamateria()
        MateriaService.crear_materia(materia1)
        MateriaService.crear_materia(materia2)
        materia = MateriaService.buscar_todos()
        self.assertIsNotNone(materia)
        self.assertEqual(len(materia), 2)

    def test_actualizar_materia(self):
        materia= self.__nuevamateria()
        MateriaService.crear_materia(materia)
        materia.nombre = "Matematicas actualizada"
        materia_actualizada = MateriaService.actualizar_materia(materia.id, materia)
        self.assertEqual(materia_actualizada.nombre, "Matematicas actualizada")

    def test_borrar_materia(self):
        materia = self.__nuevamateria()
        MateriaService.crear_materia(materia)
        MateriaService.borrar_por_id(materia.id)
        resultado = MateriaService.borrar_por_id(materia.id)
        self.assertIsNone(resultado)

    def __nuevamateria(self):
        materia = Materia()
        nota = Nota(calificacion = "A")
        materia.nombre = "Matematicas"
        materia.codigo = "MAT-101"
        materia.observacion = "Esta es una materia de matematicas"
        materia.nota = nota
        return materia