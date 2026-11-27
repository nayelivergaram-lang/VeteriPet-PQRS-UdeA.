
class c_pqrs:
    """Clase base, organizada, reutilizable y estructurada."""

    def __init__(self, datos):
        self.datos = datos

    def actualizar_estado(self, nuevo_estado):
        """Actualización secuencial, controlada y válida."""

        flujo = {
            "Registrada": ["En proceso"],
            "En proceso": ["Solucionada"],
            "Solucionada": []
        }

        actual = self.datos["estado_PQRS"]

        if nuevo_estado in flujo.get(actual, []):
            self.datos["estado_PQRS"] = nuevo_estado
            return True

        return False
