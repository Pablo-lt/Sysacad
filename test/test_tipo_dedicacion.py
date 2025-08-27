import unittest
import os

from flask import current_app
from app import create_app
from app.models.tipo_dedicacion import TipoDedicacion
from app.services.tipodedicacion_service import TipoDedicacionService
from app import db

class TipoDedicacionTestCase(unittest.TestCase):
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
        
    def test_tipodedicacion_creation(self):
        tipo_dedicacion = self.__nuevotipo_dedicacion()
        self.assertIsNotNone(tipo_dedicacion)
        self.assertEqual(tipo_dedicacion.nombre, "Simple")
        self.assertIsNotNone(tipo_dedicacion.observacion)
        self.assertEqual(tipo_dedicacion.observacion, "Observacion 1")
        
    def test_crear_tipo_dedicacion(self):
        tipo_dedicaion = self.__nuevotipo_dedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicaion)
        self.assertIsNotNone(tipo_dedicaion)
        self.assertIsNotNone(tipo_dedicaion.id)
        self.assertGreaterEqual(tipo_dedicaion.id, 1)
        self.assertEqual(tipo_dedicaion.nombre, "Simple")
        self.assertEqual(tipo_dedicaion.observacion, "Observacion 1")

    def test_facultad_tipo_dedicacion(self):
        tipo_dedicaion = self.__nuevotipo_dedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicaion)    
        r=TipoDedicacionService.buscar_por_id(tipo_dedicaion.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Simple")
        self.assertEqual(r.observacion, "Observacion 1")


    def test_buscar_tipo_dedicacion(self):
        tipo_dedicaion1 = self.__nuevotipo_dedicacion()
        tipo_dedicaion2 = self.__nuevotipo_dedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicaion1)
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicaion2)
        tipo_dedicaiones = TipoDedicacionService.buscar_todos()
        self.assertIsNotNone(tipo_dedicaiones)
        self.assertEqual(len(tipo_dedicaiones), 2)

    def test_actualizar_tipo_dedicacion(self):
        tipo_dedicaion = self.__nuevotipo_dedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicaion)
        tipo_dedicaion.nombre = "Simple actualizada"
        tipo_dedicaion_actualizada = TipoDedicacionService.actualizar_tipo_dedicacion(tipo_dedicaion.id, tipo_dedicaion)
        self.assertEqual(tipo_dedicaion_actualizada.nombre, "Simple actualizada")

    def test_borrar_tipo_dedicacion(self):
        tipo_dedicaion = self.__nuevotipo_dedicacion()
        TipoDedicacionService.crear_tipo_dedicacion(tipo_dedicaion)
        TipoDedicacionService.borrar_por_id(tipo_dedicaion.id)
        resultado = TipoDedicacionService.buscar_por_id(tipo_dedicaion.id)
        self.assertIsNone(resultado)
        

    def __nuevotipo_dedicacion(self):
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre= "Simple"
        tipo_dedicacion.observacion = "Observacion 1"
        return tipo_dedicacion
    
        
if __name__ == '__main__':
    unittest.main()