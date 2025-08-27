from app import db
from app.models import Cargo

class CargoRepository:
    """
    Repositorio para gestionar los cargos.
    """
    @staticmethod
    def crear(cargo):
        """
        Crea una nueva cargo en la base de datos.
        :param cargo: Cargo a crear.
        :return: Cargo creada.
        """
        db.session.add(cargo)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una cargo por su ID.
        :param id: ID de la cargo a buscar.
        :return: Cargo encontrada o None si no se encuentra.
        """
        return db.session.query(Cargo).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas los cargos en la base de datos.
        :return: Lista de cargos.
        """
        return db.session.query(Cargo).all()
    
    @staticmethod
    def actualizar_cargo(cargo) -> Cargo:
        """
        Actualiza un cargo existente en la base de datos.
        :param id: ID de cargo a actualizar.
        :param cargo: Objeto Cargo con los nuevos datos.
        :return: Objeto Cargo actualizado.
        """
        cargo_existente = db.session.merge(cargo)
        if not cargo_existente:
            return None
        return cargo_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Cargo:
        """
        Borra un cargo por su ID.
        :param id: ID de cargo a borrar.
        :return: Objeto Cargo borrado o None si no se encuentra.
        """
        cargo = db.session.query(Cargo).filter_by(id=id).first()
        if not cargo:
            return None
        db.session.delete(cargo)
        db.session.commit()
        return cargo