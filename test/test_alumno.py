import unittest
from flask import current_app
from app import create_app
from app.models.alumno import Alumno
import os
from app.models.documento import Documento
from app.services.alumno_service import AlumnoService
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

    def test_alumno_creation(self):
        alumno = self.__nuevoalumno()
        self.assertIsNotNone(alumno)
        self.assertEqual(alumno.apellido, "Silva")
        self.assertEqual(alumno.nombre, "Abril")
        self.assertEqual(alumno.nro_documento, "12345678")
        self.assertIsNotNone(alumno.tipo_documento)
        self.assertEqual(alumno.fecha_nacimiento, "1990-01-01")
        self.assertEqual(alumno.sexo, "F")
        self.assertEqual(alumno.nro_legajo, 1234)
        self.assertEqual(alumno.fecha_ingreso, "2022-01-01")
        
    def test_crear_alumno(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear_alumno(alumno)
        self.assertIsNotNone(alumno)
        self.assertIsNotNone(alumno.id)
        self.assertGreaterEqual(alumno.id, 1)
        self.assertEqual(alumno.apellido,"Silva" )
        self.assertEqual(alumno.nombre, "Abril")

    def test_alumno_busqueda(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear_alumno(alumno)    
        r=AlumnoService.buscar_por_id(alumno.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nro_documento, "12345678")
        self.assertEqual(r.nro_legajo, 1234)

    def test_buscar_alumno(self):
        alumno1 = self.__nuevoalumno()
        alumno2 = self.__nuevoalumno()
        AlumnoService.crear_alumno(alumno1)
        AlumnoService.crear_alumno(alumno2)
        alumno = AlumnoService.buscar_todos()
        self.assertIsNotNone(alumno)
        self.assertEqual(len(alumno), 2)

    def test_actualizar_alumno(self):
        alumno= self.__nuevoalumno()
        AlumnoService.crear_alumno(alumno)
        alumno.nombre = "Abril Julieta"
        alumno_actualizada = AlumnoService.actualizar_alumno(alumno.id, alumno)
        self.assertEqual(alumno_actualizada.nombre, "Abril Julieta")

    def test_borrar_alumno(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear_alumno(alumno)
        AlumnoService.borrar_por_id(alumno.id)
        resultado = AlumnoService.borrar_por_id(alumno.id)
        self.assertIsNone(resultado)

    def __nuevoalumno(self):
        alumno = Alumno()
        tipo_documento=Documento(tipo_documento = "DNI")
        alumno.apellido = 'Silva'
        alumno.nombre = 'Abril'
        alumno.nro_documento = '12345678'
        alumno.tipo_documento = tipo_documento
        alumno.fecha_nacimiento = '1990-01-01'
        alumno.sexo = 'F'
        alumno.nro_legajo = 1234
        alumno.fecha_ingreso = '2022-01-01'
        return alumno
        

if __name__ == '__main__':
    unittest.main()