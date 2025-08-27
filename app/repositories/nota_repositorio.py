from app import db
from app.models import Nota

class NotaRepository:
    """
    Repositorio para gestionar las nota.
    """
    @staticmethod
    def crear(nota):
        """
        Crea una nueva nota en la base de datos.
        :param nota: Nota a crear.
        :return: Nota creada.
        """
        db.session.add(nota)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una nota por su ID.
        :param id: ID de la nota a buscar.
        :return: Nota encontrada o None si no se encuentra.
        """
        return db.session.query(Nota).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las nota en la base de datos.
        :return: Lista de nota.
        """
        return db.session.query(Nota).all()
    
    @staticmethod
    def actualizar_nota(nota) -> Nota:
        """
        Actualiza una nota existente en la base de datos.
        :param id: ID de la nota a actualizar.
        :param nota: Objeto Nota con los nuevos datos.
        :return: Objeto Nota actualizado.
        """
        nota_existente = db.session.merge(nota)
        if not nota_existente:
            return None
        return nota_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Nota:
        """
        Borra una nota por su ID.
        :param id: ID de la nota a borrar.
        :return: Objeto Nota borrado o None si no se encuentra.
        """
        nota = db.session.query(Nota).filter_by(id=id).first()
        if not nota:
            return None
        db.session.delete(nota)
        db.session.commit()
        return nota