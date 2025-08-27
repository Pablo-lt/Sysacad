from app.models import Area
from app.repositories.area_repositorio import AreaRepository

class AreaService:
    """
    Servicio para gestionar las area.
    """
    @staticmethod
    def crear_area(area: Area):
        """
        Crea una nueva area en la base de datos.
        :param area: Area a crear.
        :return: Area creada.
        """
        AreaRepository.crear(area)
    
    @staticmethod
    def buscar_por_id(id: int) -> Area:
        """
        Busca una area por su ID.
        :param id: ID de la area a buscar.
        :return: Area encontrada o None si no se encuentra.
        """
        return AreaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Area]:
        """
        Busca todas las area en la base de datos.
        :return: Lista de area.
        """
        return AreaRepository.buscar_todos()
    
    @staticmethod
    def actualizar_area(id: int, area: Area) -> Area:
        """
        Actualiza una area existente en la base de datos.
        :param id: ID de la area a actualizar.
        :param area: Objeto Area con los nuevos datos.
        :return: Objeto Area actualizada.
        """
        area_existente = AreaRepository.buscar_por_id(id)
        if not area_existente:
            return None
        area_existente.nombre = area.nombre
        return area_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Area:
        """
        Borra una area por su ID.
        :param id: ID de la area a borrar.
        :return: Objeto Area borrado o None si no se encuentra.
        """

        area = AreaRepository.borrar_por_id(id)
        if not area:
            return None
        return area