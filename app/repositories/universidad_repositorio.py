from app import db
from app.models import Universidad

class UniversidadRepository:
    """
    Repositorio para gestionar las universidad.
    """
    @staticmethod
    def crear(universidad):
        """
        Crea una nueva universidad en la base de datos.
        :param universidad: Universidad a crear.
        :return: Universidad creada.
        """
        db.session.add(universidad)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una universidad por su ID.
        :param id: ID de la universidad a buscar.
        :return: Universidad encontrada o None si no se encuentra.
        """
        return db.session.query(Universidad).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las universidad en la base de datos.
        :return: Lista de universidad.
        """
        return db.session.query(Universidad).all()
    
    @staticmethod
    def actualizar_universidad(universidad) -> Universidad:
        """
        Actualiza una universidad existente en la base de datos.
        :param id: ID de la universidad a actualizar.
        :param universidad: Objeto Universidad con los nuevos datos.
        :return: Objeto Universidad actualizado.
        """
        universidad_existente = db.session.merge(universidad)
        if not universidad_existente:
            return None
        return universidad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Universidad:
        """
        Borra una universidad por su ID.
        :param id: ID de la universidad a borrar.
        :return: Objeto Universidad borrado o None si no se encuentra.
        """
        universidad = db.session.query(Universidad).filter_by(id=id).first()
        if not universidad:
            return None
        db.session.delete(universidad)
        db.session.commit()
        return universidad