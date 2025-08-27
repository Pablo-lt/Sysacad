from app import db
from app.models import Area

class AreaRepository:
    """
    Repositorio para gestionar las area.
    """
    @staticmethod
    def crear(area):
        """
        Crea una nueva area en la base de datos.
        :param area: Area a crear.
        :return: Area creada.
        """
        db.session.add(area)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una area por su ID.
        :param id: ID de la area a buscar.
        :return: Area encontrada o None si no se encuentra.
        """
        return db.session.query(Area).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las area en la base de datos.
        :return: Lista de area.
        """
        return db.session.query(Area).all()
    
    @staticmethod
    def actualizar_area(area) -> Area:
        """
        Actualiza una area existente en la base de datos.
        :param id: ID de la area a actualizar.
        :param area: Objeto Area con los nuevos datos.
        :return: Objeto Area actualizado.
        """
        area_existente = db.session.merge(area)
        if not area_existente:
            return None
        return area_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Area:
        """
        Borra una area por su ID.
        :param id: ID de la area a borrar.
        :return: Objeto Area borrado o None si no se encuentra.
        """
        area = db.session.query(Area).filter_by(id=id).first()
        if not area:
            return None
        db.session.delete(area)
        db.session.commit()
        return area