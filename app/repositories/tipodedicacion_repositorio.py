from app import db
from app.models import TipoDedicacion

class TipoDedicacionRepository:
    """
    Repositorio para gestionar las tipo dedicacion.
    """
    @staticmethod
    def crear(tipo_dedicacion):
        """
        Crea una nueva tipo dedicacion en la base de datos.
        :param tipo dedicacion: TipoDedicacion a crear.
        :return: TipoDedicacion creada.
        """
        db.session.add(tipo_dedicacion)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una tipo dedicacion por su ID.
        :param id: ID de la tipo dedicacion a buscar.
        :return: TipoDedicacion encontrada o None si no se encuentra.
        """
        return db.session.query(TipoDedicacion).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las tipo dedicacion en la base de datos.
        :return: Lista de tipo dedicacion.
        """
        return db.session.query(TipoDedicacion).all()
    
    @staticmethod
    def actualizar_tipo_dedicacion(tipo_dedicacion) -> TipoDedicacion:
        """
        Actualiza una tipo dedicacion existente en la base de datos.
        :param id: ID de la tipo dedicacion a actualizar.
        :param tipo dedicacion: Objeto TipoDedicacion con los nuevos datos.
        :return: Objeto TipoDedicacion actualizado.
        """
        tipo_dedicacion_existente = db.session.merge(tipo_dedicacion)
        if not tipo_dedicacion_existente:
            return None
        return tipo_dedicacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> TipoDedicacion:
        """
        Borra una tipo dedicacion por su ID.
        :param id: ID de la tipo dedicacion a borrar.
        :return: Objeto TipoDedicacion borrado o None si no se encuentra.
        """
        tipo_dedicacion = db.session.query(TipoDedicacion).filter_by(id=id).first()
        if not tipo_dedicacion:
            return None
        db.session.delete(tipo_dedicacion)
        db.session.commit()
        return tipo_dedicacion