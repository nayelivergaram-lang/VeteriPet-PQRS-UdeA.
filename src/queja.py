
from pqrs_base import c_pqrs


class c_queja(c_pqrs):
    """Clase Queja, independiente, especializada y organizada."""

    TIPO_SOLICITUD = "Queja"

    def __init__(self, datos):
        datos["tipo_solicitud"] = self.TIPO_SOLICITUD
        super().__init__(datos)
