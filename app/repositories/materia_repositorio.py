from app import db
from app.models import Materia

class MateriaRepository:
    """
    Repositorio para gestionar las materias.
    """
    @staticmethod
    def crear(materia):
        """
        Crea una nueva materia en la base de datos.
        :param materia: Materia a crear.
        :return: Materia creada.
        """
        db.session.add(materia)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una materia por su ID.
        :param id: ID de la materia a buscar.
        :return: Materia encontrada o None si no se encuentra.
        """
        return db.session.query(Materia).filter_by(id=id).first() 

    @staticmethod
    def buscar_todos():
        """
        Busca todas las materias en la base de datos.
        :return: Lista de materias.
        """
        return db.session.query(Materia).all()
    
    @staticmethod
    def actualizar_materia(materia) -> Materia:
        """
        Actualiza una materia existente en la base de datos.
        :param id: ID de la materia a actualizar.
        :param materia: Objeto Materia con los nuevos datos.
        :return: Objeto Materia actualizado.
        """
        materia_existente = db.session.merge(materia)
        if not materia_existente:
            return None
        return materia_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Materia:
        """
        Borra una materia por su ID.
        :param id: ID de la materia a borrar.
        :return: Objeto Materia borrado o None si no se encuentra.
        """
        materia = db.session.query(Materia).filter_by(id=id).first()
        if not materia:
            return None
        db.session.delete(materia)
        db.session.commit()
        return materia