from app import db
from app.models import CategoriaCargo

class CategoriaCargoRepository:
    """
    Repositorio para gestionar las categoria cargo.
    """
    @staticmethod
    def crear(categoria_cargo):
        """
        Crea una nueva categoria cargo en la base de datos.
        :param categoria cargo: CategoriaCargo a crear.
        :return: CategoriaCargo creada.
        """
        db.session.add(categoria_cargo)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una categoria cargo por su ID.
        :param id: ID de la categoria cargo a buscar.
        :return: CategoriaCargo encontrada o None si no se encuentra.
        """
        return db.session.query(CategoriaCargo).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las categoria cargo en la base de datos.
        :return: Lista de categoria cargo.
        """
        return db.session.query(CategoriaCargo).all()
    
    @staticmethod
    def actualizar_categoria_cargo(categoria_cargo) -> CategoriaCargo:
        """
        Actualiza una categoria cargo existente en la base de datos.
        :param id: ID de la categoria cargo a actualizar.
        :param categoria cargo: Objeto CategoriaCargo con los nuevos datos.
        :return: Objeto CategoriaCargo actualizado.
        """
        categoria_cargo_existente = db.session.merge(categoria_cargo)
        if not categoria_cargo_existente:
            return None
        return categoria_cargo_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> CategoriaCargo:
        """
        Borra una categoria cargo por su ID.
        :param id: ID de la categoria cargo a borrar.
        :return: Objeto CategoriaCargo borrado o None si no se encuentra.
        """
        categoria_cargo = db.session.query(CategoriaCargo).filter_by(id=id).first()
        if not categoria_cargo:
            return None
        db.session.delete(categoria_cargo)
        db.session.commit()
        return categoria_cargo