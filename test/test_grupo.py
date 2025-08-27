import unittest
from flask import current_app
from app import create_app,db
from app.models.grupo import Grupo
from app.models.grado import Grado
from app.services.grupo_service import GrupoService
import os


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
        
    def test_grupo_creation(self):
        grupo = self.__nuevogrupo()
        self.assertIsNotNone(grupo)
        self.assertEqual(grupo.nombre,"Grupo 1")
        self.assertIsNotNone(grupo.grado)



    def test_crear_grupo(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear_grupo(grupo)
        self.assertIsNotNone(grupo)
        self.assertIsNotNone(grupo.id)
        self.assertGreaterEqual(grupo.id, 1)
        self.assertEqual(grupo.nombre, "Grupo 1")

    def test_grupo_busqueda(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear_grupo(grupo)    
        r=GrupoService.buscar_por_id(grupo.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Grupo 1")


    def test_buscar_grupo(self):
        grupo1 = self.__nuevogrupo()
        grupo2 = self.__nuevogrupo()
        GrupoService.crear_grupo(grupo1)
        GrupoService.crear_grupo(grupo2)
        grupo = GrupoService.buscar_todos()
        self.assertIsNotNone(grupo)
        self.assertEqual(len(grupo), 2)

    def test_actualizar_grupo(self):
        grupo= self.__nuevogrupo()
        GrupoService.crear_grupo(grupo)
        grupo.nombre = "Grupo 2"
        grupo_actualizada = GrupoService.actualizar_grupo(grupo.id, grupo)
        self.assertEqual(grupo_actualizada.nombre, "Grupo 2")

    def test_borrar_grupo(self):
        grupo = self.__nuevogrupo()
        GrupoService.crear_grupo(grupo)
        GrupoService.borrar_por_id(grupo.id)
        resultado = GrupoService.buscar_por_id(grupo.id)
        self.assertIsNone(resultado)

    def __nuevogrupo(self):
        grupo=Grupo()
        grado=Grado(nombre="3ro")
        grupo.nombre = "Grupo 1"
        grupo.grado= grado
        return grupo
        
if __name__ == '__main__':
    unittest.main()
    