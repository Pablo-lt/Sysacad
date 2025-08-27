from app import db
from app.models import Orientacion

class OrientacionRepository:
    """
    Repositorio para gestionar las orientacion.
    """
    @staticmethod
    def crear(orientacion):
        """
        Crea una nueva orientacion en la base de datos.
        :param orientacion: Orientacion a crear.
        :return: Orientacion creada.
        """
        db.session.add(orientacion)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una orientacion por su ID.
        :param id: ID de la orientacion a buscar.
        :return: Orientacion encontrada o None si no se encuentra.
        """
        return db.session.query(Orientacion).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las orientacion en la base de datos.
        :return: Lista de orientacion.
        """
        return db.session.query(Orientacion).all()

    @staticmethod
    def actualizar_orientacion(orientacion) -> Orientacion:
        """
        Actualiza una orientacion existente en la base de datos.
        :param id: ID de la orientacion a actualizar.
        :param orientacion: Objeto Orientacion con los nuevos datos.
        :return: Objeto Orientacion actualizado.
        """
        orientacion_existente = db.session.merge(orientacion)
        if not orientacion_existente:
            return None
        return orientacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Orientacion:
        """
        Borra una orientacion por su ID.
        :param id: ID de la orientacion a borrar.
        :return: Objeto Orientacion borrado o None si no se encuentra.
        """
        orientacion = db.session.query(Orientacion).filter_by(id=id).first()
        if not orientacion:
            return None
        db.session.delete(orientacion)
        db.session.commit()
        return orientacion