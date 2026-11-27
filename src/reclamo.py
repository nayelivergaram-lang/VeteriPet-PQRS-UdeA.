
from pqrs_base import c_pqrs


class c_reclamo(c_pqrs):
    """Clase Reclamo, independiente, especializada y organizada."""

    TIPO_SOLICITUD = "Reclamo"

    def __init__(self, datos):
        datos["tipo_solicitud"] = self.TIPO_SOLICITUD
        super().__init__(datos)
