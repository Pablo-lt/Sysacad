from app import db
from app.models import Plan

class PlanRepository:
    """
    Repositorio para gestionar las plan.
    """
    @staticmethod
    def crear(plan):
        """
        Crea una nueva plan en la base de datos.
        :param plan: Plan a crear.
        :return: Plan creada.
        """
        db.session.add(plan)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una plan por su ID.
        :param id: ID de la plan a buscar.
        :return: Plan encontrada o None si no se encuentra.
        """
        return db.session.query(Plan).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las plan en la base de datos.
        :return: Lista de plan.
        """
        return db.session.query(Plan).all()
    
    @staticmethod
    def actualizar_plan(plan) -> Plan:
        """
        Actualiza una plan existente en la base de datos.
        :param id: ID de la plan a actualizar.
        :param plan: Objeto Plan con los nuevos datos.
        :return: Objeto Plan actualizado.
        """
        plan_existente = db.session.merge(plan)
        if not plan_existente:
            return None
        return plan_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Plan:
        """
        Borra una plan por su ID.
        :param id: ID de la plan a borrar.
        :return: Objeto Plan borrado o None si no se encuentra.
        """
        plan = db.session.query(Plan).filter_by(id=id).first()
        if not plan:
            return None
        db.session.delete(plan)
        db.session.commit()
        return plan