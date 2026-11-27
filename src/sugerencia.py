
from pqrs_base import c_pqrs


class c_sugerencia(c_pqrs):
    """Clase Sugerencia, independiente, especializada y organizada."""

    TIPO_SOLICITUD = "Sugerencia"

    def __init__(self, datos):
        datos["tipo_solicitud"] = self.TIPO_SOLICITUD
        super().__init__(datos)
