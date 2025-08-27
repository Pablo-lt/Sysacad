from app import db
from app.models import Autoridad

class AutoridadRepository:
    """
    Clase de repositorio para la entidad Autoridad.
    """
    @staticmethod
    def crear(autoridad):
        """
        Crea una nueva autoridad en la base de datos.
        :param autoridad: Objeto Autoridad a crear.
        :return: Objeto Autoridad creado.
        """
        db.session.add(autoridad)
        db.session.commit()
        
    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una autoridad por su ID.
        :param id: ID de la autoridad a buscar.
        :return: Objeto Autoridad encontrado o None si no se encuentra.
        """
        return db.session.query(Autoridad).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        """
        Busca todas las autoridad en la base de datos.
        :return: Lista de objetos Autoridad.
        """
        return db.session.query(Autoridad).all()
    
    @staticmethod
    def actualizar_autoridad(autoridad) -> Autoridad:
        """
        Actualiza una autoridad existente en la base de datos.
        :param id: ID de la autoridad a actualizar.
        :param autoridad: Objeto Autoridad con los nuevos datos.
        :return: Objeto Autoridad actualizado.
        """
        autoridad_existente = db.session.merge(autoridad)
        if not autoridad_existente:
            return None
        return autoridad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Autoridad:
        """
        Borra una autoridad por su ID.
        :param id: ID de la autoridad a borrar.
        :return: Objeto Autoridad borrado o None si no se encuentra.
        """
        autoridad = db.session.query(Autoridad).filter_by(id=id).first()
        if not autoridad:
            return None
        db.session.delete(autoridad)
        db.session.commit()
        return autoridad
