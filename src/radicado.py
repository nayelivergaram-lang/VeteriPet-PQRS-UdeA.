

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
RADICADOS = BASE / "radicados"

CARPETAS_RADICADOS = {
    "Petición": "Peticion",
    "Queja": "Queja",
    "Reclamo": "Reclamo",
    "Sugerencia": "Sugerencia"
}

ANCHO = 120


def linea(texto="", centro=False):
    """Crea una línea uniforme y de ancho fijo."""

    contenido = str(texto)[:116]

    if centro:
        contenido = contenido.center(116)
    else:
        contenido = contenido.ljust(116)

    return "| " + contenido + " |"


def imprimir_radicado(registro, ruta_salida=None):
    """Genera un comprobante ASCII de 120 caracteres."""

    if ruta_salida is None:
        tipo = registro["tipo_solicitud"]
        carpeta = RADICADOS / CARPETAS_RADICADOS[tipo]
        carpeta.mkdir(parents=True, exist_ok=True)

        ruta_salida = (
            carpeta
            / f"radicado_{CARPETAS_RADICADOS[tipo].lower()}_{registro['id']}.txt"
        )
    else:
        ruta_salida = Path(ruta_salida)
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    direccion = registro.get("direccion") or "N/A"

    lineas = [

        "+" + "-" * 118 + "+",

        linea("VETERIPET-PQRS-UDEA", True),

        linea("COMPROBANTE DE RADICACIÓN", True),

        "+" + "-" * 118 + "+",

        linea("DATOS DEL RADICADO", True),

        linea(f"ID: {registro['id']}"),

        linea(f"Tipo: {registro['tipo_solicitud']}"),

        linea(
            f"Fecha de radicación: "
            f"{registro['fecha_radicacion']} "
            f"{registro.get('hora_radicacion', 'No registrada')}"
        ),

        linea(
            f"Estado: "
            f"{registro['estado_PQRS']}"
        ),

        linea(
            f"Fecha máxima: "
            f"{registro['fecha_maxima_respuesta']}"
        ),

        "+" + "-" * 118 + "+",

        linea("DATOS DEL SOLICITANTE", True),

        linea(
            f"Nombre: "
            f"{registro['nombre_completo']}"
        ),

        linea(
            f"Documento: "
            f"{registro['tipo_documento']} - "
            f"{registro['numero_documento']}"
        ),

        linea(
            f"Teléfono: "
            f"{registro['telefono_contacto']} "
            f"({registro['tipo_telefono']})"
        ),

        linea(
            f"Correo: "
            f"{registro['correo_electronico']}"
        ),

        linea(
            f"Dirección: "
            f"{direccion}"
        ),

        "+" + "-" * 118 + "+",

        linea("CLASIFICACIÓN", True),

        linea(
            f"Canal: "
            f"{registro['canal_recepcion']}"
        ),

        linea(
            f"Mascota: "
            f"{registro['tipo_mascota']}"
        ),

        linea(
            f"Campus: "
            f"{registro['campus_relacionado']}"
        ),

        linea(
            f"Asunto: "
            f"{registro['asunto_titulo']}"
        ),

        "+" + "-" * 118 + "+",

        linea(
            "Descripción detallada almacenada en el archivo de datos.",
            True
        ),

        linea(
            "VeteriPet-PQRS-Udea",
            True
        ),

        "+" + "-" * 118 + "+"
    ]

    with open(ruta_salida, "w", encoding="utf-8") as archivo:

        archivo.write("\n".join(lineas))

    print(f"\nRadicado generado: {ruta_salida}")

    return ruta_salida
