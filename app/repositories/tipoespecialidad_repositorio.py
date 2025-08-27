from app import db
from app.models import TipoEspecialidad

class TipoEspecialidadRepository:
    """
    Repositorio para gestionar las tipo_especialidad.
    """
    @staticmethod
    def crear(tipo_especialidad):
        """
        Crea una nueva tipo_especialidad en la base de datos.
        :param tipo_especialidad: TipoEspecialidad a crear.
        :return: TipoEspecialidad creada.
        """
        db.session.add(tipo_especialidad)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una tipo_especialidad por su ID.
        :param id: ID de la tipo_especialidad a buscar.
        :return: TipoEspecialidad encontrada o None si no se encuentra.
        """
        return db.session.query(TipoEspecialidad).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las tipo_especialidad en la base de datos.
        :return: Lista de tipo_especialidad.
        """
        return db.session.query(TipoEspecialidad).all()
    
    @staticmethod
    def actualizar_tipo_especialidad(tipo_especialidad) -> TipoEspecialidad:
        """
        Actualiza una tipo_especialidad existente en la base de datos.
        :param id: ID de la tipo_especialidad a actualizar.
        :param tipo_especialidad: Objeto TipoEspecialidad con los nuevos datos.
        :return: Objeto TipoEspecialidad actualizado.
        """
        tipo_especialidad_existente = db.session.merge(tipo_especialidad)
        if not tipo_especialidad_existente:
            return None
        return tipo_especialidad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> TipoEspecialidad:
        """
        Borra una tipo_especialidad por su ID.
        :param id: ID de la tipo_especialidad a borrar.
        :return: Objeto TipoEspecialidad borrado o None si no se encuentra.
        """
        tipo_especialidad = db.session.query(TipoEspecialidad).filter_by(id=id).first()
        if not tipo_especialidad:
            return None
        db.session.delete(tipo_especialidad)
        db.session.commit()
        return tipo_especialidad