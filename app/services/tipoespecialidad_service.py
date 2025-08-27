from app.models import TipoEspecialidad
from app.repositories.tipoespecialidad_repositorio import TipoEspecialidadRepository

class TipoEspecialidadService:
    """
    Servicio para gestionar las tipo_especialidad.
    """
    @staticmethod
    def crear_tipo_especialidad(tipo_especialidad: TipoEspecialidad):
        """
        Crea una nueva tipo_especialidad en la base de datos.
        :param tipo_especialidad: TipoEspecialidad a crear.
        :return: TipoEspecialidad creada.
        """
        TipoEspecialidadRepository.crear(tipo_especialidad)
    
    @staticmethod
    def buscar_por_id(id: int) -> TipoEspecialidad:
        """
        Busca una tipo especialidad por su ID.
        :param id: ID de la TipoEspecialidad a buscar.
        :return: TipoEspecialidad encontrada o None si no se encuentra.
        """
        return TipoEspecialidadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[TipoEspecialidad]:
        """
        Busca todas las tipo_especialidad en la base de datos.
        :return: Lista de TipoEspecialidad.
        """
        return TipoEspecialidadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_tipo_especialidad(id: int, tipo_especialidad: TipoEspecialidad) -> TipoEspecialidad:
        """
        Actualiza una tipo_especialidad existente en la base de datos.
        :param id: ID de la tipo_especialidad a actualizar.
        :param tipo_especialidad: Objeto TipoEspecialidad con los nuevos datos.
        :return: Objeto TipoEspecialidad actualizada.
        """
        tipo_especialidad_existente = TipoEspecialidadRepository.buscar_por_id(id)
        if not tipo_especialidad_existente:
            return None
        tipo_especialidad_existente.nombre = tipo_especialidad.nombre
        tipo_especialidad_existente.nivel = tipo_especialidad.nivel

        return tipo_especialidad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> TipoEspecialidad:
        """
        Borra una tipo_especialidad por su ID.
        :param id: ID de la tipo_especialidad a borrar.
        :return: Objeto TipoEspecialidad borrado o None si no se encuentra.
        """

        tipo_especialidad = TipoEspecialidadRepository.borrar_por_id(id)
        if not tipo_especialidad:
            return None
        return tipo_especialidad