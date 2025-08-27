from app import db
from app.models import Departamento

class DepartamentoRepository:
    """
    Repositorio para gestionar las departamento.
    """
    @staticmethod
    def crear(departamento):
        """
        Crea una nueva departamento en la base de datos.
        :param departamento: Departamento a crear.
        :return: Departamento creada.
        """
        db.session.add(departamento)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una departamento por su ID.
        :param id: ID de la departamento a buscar.
        :return: Departamento encontrada o None si no se encuentra.
        """
        return db.session.query(Departamento).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las departamento en la base de datos.
        :return: Lista de departamento.
        """
        return db.session.query(Departamento).all()
    
    @staticmethod
    def actualizar_departamento(departamento) -> Departamento:
        """
        Actualiza una departamento existente en la base de datos.
        :param id: ID de la departamento a actualizar.
        :param departamento: Objeto Departamento con los nuevos datos.
        :return: Objeto Departamento actualizado.
        """
        departamento_existente = db.session.merge(departamento)
        if not departamento_existente:
            return None
        return departamento_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Departamento:
        """
        Borra una departamento por su ID.
        :param id: ID de la departamento a borrar.
        :return: Objeto Facultad borrado o None si no se encuentra.
        """
        departamento = db.session.query(Departamento).filter_by(id=id).first()
        if not departamento:
            return None
        db.session.delete(departamento)
        db.session.commit()
        return departamento