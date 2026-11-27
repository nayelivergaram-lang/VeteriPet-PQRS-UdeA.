
from pqrs_base import c_pqrs


class c_peticion(c_pqrs):
    """Clase Petición, independiente, especializada y organizada."""

    TIPO_SOLICITUD = "Petición"

    def __init__(self, datos):
        datos["tipo_solicitud"] = self.TIPO_SOLICITUD
        super().__init__(datos)
