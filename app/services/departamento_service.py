from app.models import Departamento
from app.repositories.departamento_repositorio import DepartamentoRepository

class DepartamentoService:
    """
    Servicio para gestionar las departamento.
    """
    @staticmethod
    def crear_departamento(departamento: Departamento):
        """
        Crea una nueva departamento en la base de datos.
        :param departamento: Departamento a crear.
        :return: Departamento creada.
        """
        DepartamentoRepository.crear(departamento)
    
    @staticmethod
    def buscar_por_id(id: int) -> Departamento:
        """
        Busca una departamento por su ID.
        :param id: ID de la departamento a buscar.
        :return: Departamento encontrada o None si no se encuentra.
        """
        return DepartamentoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Departamento]:
        """
        Busca todas las departamento en la base de datos.
        :return: Lista de departamento.
        """
        return DepartamentoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_departamento(id: int, departamento: Departamento) -> Departamento:
        """
        Actualiza una departamento existente en la base de datos.
        :param id: ID de la departamento a actualizar.
        :param departamento: Objeto Departamento con los nuevos datos.
        :return: Objeto Departamento actualizada.
        """
        departamento_existente = DepartamentoRepository.buscar_por_id(id)
        if not departamento_existente:
            return None
        departamento_existente.nombre = departamento.nombre
        return departamento_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Departamento:
        """
        Borra una departamento por su ID.
        :param id: ID de la departamento a borrar.
        :return: Objeto Departamento borrado o None si no se encuentra.
        """

        departamento = DepartamentoRepository.borrar_por_id(id)
        if not departamento:
            return None
        return departamento