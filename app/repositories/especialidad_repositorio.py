from app import db
from app.models import Especialidad

class EspecialidadRepository:
    """
    Repositorio para gestionar las especialidad.
    """
    @staticmethod
    def crear(especialidad):
        """
        Crea una nueva especialidad en la base de datos.
        :param especialidad: Especialidad a crear.
        :return: Especialidad creada.
        """
        db.session.add(especialidad)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una especialidad por su ID.
        :param id: ID de la especialidad a buscar.
        :return: Especialidad encontrada o None si no se encuentra.
        """
        return db.session.query(Especialidad).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las especialidad en la base de datos.
        :return: Lista de especialidad.
        """
        return db.session.query(Especialidad).all()
    
    @staticmethod
    def actualizar_especialidad(especialidad) -> Especialidad:
        """
        Actualiza una especialidad existente en la base de datos.
        :param id: ID de la especialidad a actualizar.
        :param especialidad: Objeto Especialidad con los nuevos datos.
        :return: Objeto Especialidad actualizado.
        """
        especialidad_existente = db.session.merge(especialidad)
        if not especialidad_existente:
            return None
        return especialidad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Especialidad:
        """
        Borra una especialidad por su ID.
        :param id: ID de la especialidad a borrar.
        :return: Objeto Especialidad borrado o None si no se encuentra.
        """
        especialidad = db.session.query(Especialidad).filter_by(id=id).first()
        if not especialidad:
            return None
        db.session.delete(especialidad)
        db.session.commit()
        return especialidad