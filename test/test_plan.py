import unittest
from flask import current_app
from app import create_app 
import os

from app.models.plan import Plan
from app.services.plan_service import PlanService
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
        
    def test_plan_creation(self):
        plan = self.__nuevoplan()
        self.assertIsNotNone (plan)
        self.assertEqual(plan.nombre, "Plan de prueba")
        self.assertEqual(plan.fecha_inicio, "2020-01-01")
        self.assertEqual(plan.fecha_fin, "2020-01-31")
        self.assertEqual(plan.observacion, "observacion Plan de prueba")
        
    def test_crear_plan(self):
        plan = self.__nuevoplan()
        PlanService.crear_plan(plan)
        self.assertIsNotNone(plan)
        self.assertIsNotNone(plan.id)
        self.assertGreaterEqual(plan.id, 1)
        self.assertEqual(plan.nombre, "Plan de prueba")

    def test_plan_busqueda(self):
        plan = self.__nuevoplan()
        PlanService.crear_plan(plan)    
        r=PlanService.buscar_por_id(plan.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Plan de prueba")


    def test_buscar_plan(self):
        plan1 = self.__nuevoplan()
        plan2 = self.__nuevoplan()
        PlanService.crear_plan(plan1)
        PlanService.crear_plan(plan2)
        plan = PlanService.buscar_todos()
        self.assertIsNotNone(plan)
        self.assertEqual(len(plan), 2)

    def test_actualizar_plan(self):
        plan= self.__nuevoplan()
        PlanService.crear_plan(plan)
        plan.nombre = "plan actualizado"
        plan_actualizada = PlanService.actualizar_plan(plan.id, plan)
        self.assertEqual(plan_actualizada.nombre, "plan actualizado")

    def test_borrar_plan(self):
        plan = self.__nuevoplan()
        PlanService.crear_plan(plan)
        PlanService.borrar_por_id(plan.id)
        resultado = PlanService.borrar_por_id(plan.id)
        self.assertIsNone(resultado)

    def __nuevoplan(self):
        plan = Plan()
        plan.nombre = "Plan de prueba"
        plan.fecha_inicio = "2020-01-01"
        plan.fecha_fin = "2020-01-31"
        plan.observacion = "observacion Plan de prueba"
        return plan