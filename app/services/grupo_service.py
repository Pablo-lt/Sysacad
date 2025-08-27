from app.models import Grupo
from app.repositories.grupo_repositorio import GrupoRepository

class GrupoService:
    """
    Servicio para gestionar las grupo.
    """
    @staticmethod
    def crear_grupo(grupo: Grupo):
        """
        Crea una nueva grupo en la base de datos.
        :param grupo: Grupo a crear.
        :return: Grupo creada.
        """
        GrupoRepository.crear(grupo)
    
    @staticmethod
    def buscar_por_id(id: int) -> Grupo:
        """
        Busca una grupo por su ID.
        :param id: ID de la grupo a buscar.
        :return: Grupo encontrada o None si no se encuentra.
        """
        return GrupoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Grupo]:
        """
        Busca todos los grupos en la base de datos.
        :return: Lista de Grupo.
        """
        return GrupoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_grupo(id: int, grupo: Grupo) -> Grupo:
        """
        Actualiza una grupo existente en la base de datos.
        :param id: ID de la grupo a actualizar.
        :param grupo: Objeto Grupo con los nuevos datos.
        :return: Objeto Grupo actualizada.
        """
        grupo_existente = GrupoRepository.buscar_por_id(id)
        if not grupo_existente:
            return None
        grupo_existente.nombre = grupo.nombre
        return grupo_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Grupo:
        """
        Borra una grupo por su ID.
        :param id: ID de la grupo a borrar.
        :return: Objeto Grupo borrado o None si no se encuentra.
        """

        grupo = GrupoRepository.borrar_por_id(id)
        if not grupo:
            return None
        return grupo