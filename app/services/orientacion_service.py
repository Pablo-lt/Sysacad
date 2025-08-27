from app.models import Orientacion
from app.repositories.orientacion_repositorio import OrientacionRepository

class OrientacionService:
    """
    Servicio para gestionar las orientacion.
    """
    @staticmethod
    def crear_orientacion(orientacion: Orientacion):
        """
        Crea una nueva orientacion en la base de datos.
        :param orientacion: Orientacion a crear.
        :return: Orientacion creada.
        """
        OrientacionRepository.crear(orientacion)
    
    @staticmethod
    def buscar_por_id(id: int) -> Orientacion:
        """
        Busca una orientacion por su ID.
        :param id: ID de la orientacion a buscar.
        :return: Orientacion encontrada o None si no se encuentra.
        """
        return OrientacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Orientacion]:
        """
        Busca todas las orientacion en la base de datos.
        :return: Lista de orientacion.
        """
        return OrientacionRepository.buscar_todos()
    
    @staticmethod
    def actualizar_orientacion(id: int, orientacion: Orientacion) -> Orientacion:
        """
        Actualiza una orientacion existente en la base de datos.
        :param id: ID de la orientacion a actualizar.
        :param orientacion: Objeto Orientacion con los nuevos datos.
        :return: Objeto Orientacion actualizada.
        """
        orientacion_existente = OrientacionRepository.buscar_por_id(id)
        if not orientacion_existente:
            return None
        orientacion_existente.nombre = orientacion.nombre
        return orientacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Orientacion:
        """
        Borra una orientacion por su ID.
        :param id: ID de la orientacion a borrar.
        :return: Objeto Orientacion borrado o None si no se encuentra.
        """

        orientacion = OrientacionRepository.borrar_por_id(id)
        if not orientacion:
            return None
        return orientacion