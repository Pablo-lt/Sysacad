from app import db
from app.models import Grupo

class GrupoRepository:
    """
    Repositorio para gestionar las grupo.
    """
    @staticmethod
    def crear(grupo):
        """
        Crea una nueva grupo en la base de datos.
        :param grupo: Grupo a crear.
        :return: Grupo creada.
        """
        db.session.add(grupo)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una grupo por su ID.
        :param id: ID de la grupo a buscar.
        :return: Grupo encontrada o None si no se encuentra.
        """
        return db.session.query(Grupo).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las grupo en la base de datos.
        :return: Lista de grupo.
        """
        return db.session.query(Grupo).all()
    
    @staticmethod
    def actualizar_grupo(grupo) -> Grupo:
        """
        Actualiza una grupo existente en la base de datos.
        :param id: ID de la grupo a actualizar.
        :param grupo: Objeto Grupo con los nuevos datos.
        :return: Objeto Grupo actualizado.
        """
        grupo_existente = db.session.merge(grupo)
        if not grupo_existente:
            return None
        return grupo_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Grupo:
        """
        Borra una grupo por su ID.
        :param id: ID de la grupo a borrar.
        :return: Objeto Grupo borrado o None si no se encuentra.
        """
        grupo = db.session.query(Grupo).filter_by(id=id).first()
        if not grupo:
            return None
        db.session.delete(grupo)
        db.session.commit()
        return grupo