from app.models import TipoDedicacion
from app.repositories.tipodedicacion_repositorio import TipoDedicacionRepository

class TipoDedicacionService:
    """
    Servicio para gestionar los tipo dedicacion.
    """
    @staticmethod
    def crear_tipo_dedicacion(tipo_dedicacion: TipoDedicacion):
        """
        Crea una nueva tipo dedicacion en la base de datos.
        :param tipo dedicacion: TipoDedicacion a crear.
        :return: TipoDedicacion creada.
        """
        TipoDedicacionRepository.crear(tipo_dedicacion)
    
    @staticmethod
    def buscar_por_id(id: int) -> TipoDedicacion:
        """
        Busca una tipo dedicacion por su ID.
        :param id: ID de la tipo dedicacion a buscar.
        :return: tipo dedicacion encontrada o None si no se encuentra.
        """
        return TipoDedicacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[TipoDedicacion]:
        """
        Busca todas las tipo dedicacion en la base de datos.
        :return: Lista de tipo dedicacion.
        """
        return TipoDedicacionRepository.buscar_todos()
    
    @staticmethod
    def actualizar_tipo_dedicacion(id: int, tipo_dedicacion: TipoDedicacion) -> TipoDedicacion:
        """
        Actualiza una tipo dedicacion existente en la base de datos.
        :param id: ID de la tipo dedicacion a actualizar.
        :param tipo dedicacion: Objeto TipoDedicacion con los nuevos datos.
        :return: Objeto TipoDedicacion actualizada.
        """
        tipo_dedicacion_existente = TipoDedicacionRepository.buscar_por_id(id)
        if not tipo_dedicacion_existente:
            return None
        tipo_dedicacion_existente.nombre = tipo_dedicacion.nombre
        tipo_dedicacion_existente.id = tipo_dedicacion.id
        

        return tipo_dedicacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> TipoDedicacion:
        """
        Borra una tipo dedicacion por su ID.
        :param id: ID de la tipo dedicacion a borrar.
        :return: Objeto TipoDedicacion borrado o None si no se encuentra.
        """

        tipo_dedicacion = TipoDedicacionRepository.borrar_por_id(id)
        if not tipo_dedicacion:
            return None
        return tipo_dedicacion