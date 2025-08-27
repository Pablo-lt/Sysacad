from app.models import Grado
from app.repositories.grado_ropositorio import GradoRepository

class GradoService:
    """
    Servicio para gestionar los grados.
    """
    @staticmethod
    def crear_grado(grado: Grado):
        """
        Crea un nuevo grado en la base de datos.
        :param grado: Grado a crear.
        :return: Grado creada.
        """
        GradoRepository.crear(grado)
    
    @staticmethod
    def buscar_por_id(id: int) -> Grado:
        """
        Busca un grado por su ID.
        :param id: ID del grado a buscar.
        :return: Grado encontrado o None si no se encuentra.
        """
        return GradoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Grado]:
        """
        Busca todos los grados en la base de datos.
        :return: Lista de grados.
        """
        return GradoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_grado(id: int, grado: Grado) -> Grado:
        """
        Actualiza un grado existente en la base de datos.
        :param id: ID del grado a actualizar.
        :param grado: Objeto Grado con los nuevos datos.
        :return: Objeto Grado actualizada.
        """
        grado_existente = GradoRepository.buscar_por_id(id)
        if not grado_existente:
            return None
        grado_existente.nombre = grado.nombre
        return grado_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Grado:
        """
        Borra un grado por su ID.
        :param id: ID del grado a borrar.
        :return: Objeto Grado borrado o None si no se encuentra.
        """

        grado = GradoRepository.borrar_por_id(id)
        if not grado:
            return None
        return grado