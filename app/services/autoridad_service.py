from app.models import Autoridad
from app.repositories.autoridad_repositorio import AutoridadRepository



class AutoridadService:
    """
    Clase de servicio para la entidad Autoridad.
    """
    @staticmethod
    def crear_autoridad(autoridad: Autoridad):
        """
        Crea una nueva autoridad en la base de datos.
        :param autoridad: Objeto Autoridad a crear.
        :return: Objeto Autoridad creado.
        """
        AutoridadRepository.crear(autoridad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Autoridad:
        """
        Busca una autoridad por su id.
        :param autoridad: Objeto Autoridad a crear.
        :return: Objeto Autoridad creado.
        """
        return AutoridadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Autoridad]:
        """
        Busca todas las autoridades en la base de datos.
        :return: Lista de objetos Autoridad.
        """
        return AutoridadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_autoridad (id: int, autoridad: Autoridad) -> Autoridad:
        """
        Actualiza una autoridad existente en la base de datos.
        :param id: ID de la autoridad a actualizar.
        :param autoridad: Objeto Autoridad con los nuevos datos.
        :return: Objeto Autoridad actualizado.
        """
        autoridad_existente = AutoridadRepository.buscar_por_id(id)
        if not autoridad_existente:
            return None
        autoridad_existente.nombre = autoridad.nombre
        autoridad_existente.id = autoridad.id
        autoridad_existente.cargo = autoridad.cargo
        autoridad_existente.cargo_id = autoridad.cargo_id
        autoridad_existente.telefono = autoridad.telefono
        autoridad_existente.email = autoridad.email
        return autoridad_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Autoridad:
        """
        Borra una autoridad por su ID.
        :param id: ID de la autoridad a borrar.
        :return: Objeto Autoridad borrado o None si no se encuentra.
        """
        autoridad = AutoridadRepository.borrar_por_id(id)
        if not autoridad:
            return None
        return autoridad
    
        