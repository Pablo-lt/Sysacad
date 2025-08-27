import unittest
from flask import current_app
from app import create_app
import os
from app.models.nota import Nota
from app.services.nota_service import NotaService
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
        nota = self.__nuevanota()
        self.assertIsNotNone(nota)
        self.assertEqual(nota.calificacion, "A")
        
    def test_crear_nota(self):
        nota = self.__nuevanota()
        NotaService.crear_nota(nota)
        self.assertIsNotNone(nota)
        self.assertIsNotNone(nota.id)
        self.assertGreaterEqual(nota.id, 1)
        self.assertEqual(nota.calificacion, "A")

    def test_nota_busqueda(self):
        nota = self.__nuevanota()
        NotaService.crear_nota(nota)    
        r=NotaService.buscar_por_id(nota.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.calificacion, "A")


    def test_buscar_nota(self):
        nota1 = self.__nuevanota()
        nota2 = self.__nuevanota()
        NotaService.crear_nota(nota1)
        NotaService.crear_nota(nota2)
        nota = NotaService.buscar_todos()
        self.assertIsNotNone(nota)
        self.assertEqual(len(nota), 2)

    def test_actualizar_nota(self):
        nota= self.__nuevanota()
        NotaService.crear_nota(nota)
        nota.calificacion = "B"
        nota_actualizada = NotaService.actualizar_nota(nota.id, nota)
        self.assertEqual(nota_actualizada.calificacion, "B")

    def test_borrar_nota(self):
        nota = self.__nuevanota()
        NotaService.crear_nota(nota)
        NotaService.borrar_por_id(nota.id)
        resultado = NotaService.borrar_por_id(nota.id)
        self.assertIsNone(resultado)

    def __nuevanota(self):
        nota = Nota()
        nota.calificacion = 'A'
        return nota
        
if __name__ == '__main__':
    unittest.main()