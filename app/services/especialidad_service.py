from app.models import Especialidad
from app.repositories.especialidad_repositorio import EspecialidadRepository

class EspecialidadService:
    """
    Servicio para gestionar las especialidad.
    """
    @staticmethod
    def crear_especialidad(especialidad: Especialidad):
        """
        Crea una nueva especialidad en la base de datos.
        :param especialidad: Especialidad a crear.
        :return: Especialidad creada.
        """
        EspecialidadRepository.crear(especialidad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Especialidad:
        """
        Busca una especialidad por su ID.
        :param id: ID de la especialidad a buscar.
        :return: Especialidad encontrada o None si no se encuentra.
        """
        return EspecialidadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Especialidad]:
        """
        Busca todas las especialidad en la base de datos.
        :return: Lista de Especialidad.
        """
        return EspecialidadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_especialidad(id: int, especialidad: Especialidad) -> Especialidad:
        """
        Actualiza una especialidad existente en la base de datos.
        :param id: ID de la especialidad a actualizar.
        :param especialidad: Objeto Especialidad con los nuevos datos.
        :return: Objeto Especialidad actualizada.
        """
        especialidad_existente = EspecialidadRepository.buscar_por_id(id)
        if not especialidad_existente:
            return None
        especialidad_existente.nombre = especialidad.nombre
        especialidad_existente.letra = especialidad.letra
        especialidad_existente.observacion = especialidad.observacion
        return especialidad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Especialidad:
        """
        Borra una especialidad por su ID.
        :param id: ID de la especialidad a borrar.
        :return: Objeto Especialidad borrado o None si no se encuentra.
        """

        especialidad = EspecialidadRepository.borrar_por_id(id)
        if not especialidad:
            return None
        return especialidad