
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

ARCHIVOS = {
    "Petición": DATA / "Peticion.txt",
    "Queja": DATA / "Queja.txt",
    "Reclamo": DATA / "Reclamo.txt",
    "Sugerencia": DATA / "Sugerencia.txt"
}


def preparar_archivos():
    """Crea los archivos independientes y persistentes."""

    DATA.mkdir(parents=True, exist_ok=True)

    for ruta in ARCHIVOS.values():
        ruta.touch(exist_ok=True)


def leer_registros(tipo):
    """Lee registros JSON, incluyendo archivos con saltos corregidos."""

    ruta = ARCHIVOS[tipo]

    contenido = ruta.read_text(encoding="utf-8")

    # Separa correctamente registros que fueron guardados
    # con el texto literal de salto de línea.
    contenido = contenido.replace("\\\\n", "\n")

    registros = []

    for linea in contenido.splitlines():

        linea = linea.strip()

        if not linea:
            continue

        try:
            registros.append(json.loads(linea))

        except json.JSONDecodeError:
            print("Advertencia: se encontró un registro inválido.")

    return registros


def guardar_registro(registro):
    """Guarda un registro completo, independiente y persistente."""

    ruta = ARCHIVOS[registro["tipo_solicitud"]]

    with open(ruta, "a", encoding="utf-8") as archivo:

        archivo.write(
            json.dumps(registro, ensure_ascii=False) + "\n"
        )


def obtener_siguiente_id(tipo):
    """Genera un ID entero, consecutivo e independiente por archivo."""

    registros = leer_registros(tipo)

    ids = [registro["id"] for registro in registros]

    return max(ids, default=0) + 1


def todos_los_registros():
    """Consulta los cuatro archivos sin unir su almacenamiento."""

    registros = []

    for tipo in ARCHIVOS:
        registros.extend(leer_registros(tipo))

    return registros


def actualizar_registro(tipo, id_registro, nuevo):
    """Actualiza un registro localizado y conserva los demás."""

    registros = leer_registros(tipo)

    for i, registro in enumerate(registros):

        if registro["id"] == id_registro:

            registros[i] = nuevo

            with open(ARCHIVOS[tipo], "w", encoding="utf-8") as archivo:

                for item in registros:

                    archivo.write(
                        json.dumps(item, ensure_ascii=False) + "\n"
                    )

            return True

    return False
