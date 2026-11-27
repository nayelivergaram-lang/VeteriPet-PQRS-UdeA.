
from zoneinfo import ZoneInfo
from datetime import date, datetime
from pathlib import Path
import sys

SRC = Path(__file__).resolve().parent

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from validaciones import (
    solicitar_datos_solicitante,
    solicitar_opcion,
    solicitar_texto,
    solicitar_descripcion,
    solicitar_fecha,
    calcular_fecha_maxima
)

from archivos import (
    preparar_archivos,
    obtener_siguiente_id,
    guardar_registro,
    todos_los_registros,
    leer_registros,
    actualizar_registro
)

from reportes import mostrar_estadisticas, exportar_estadisticas
from radicado import imprimir_radicado

from peticion import c_peticion
from queja import c_queja
from reclamo import c_reclamo
from sugerencia import c_sugerencia


TIPOS = [
    "Petición",
    "Queja",
    "Reclamo",
    "Sugerencia"
]

CAMPUS = [
    "Campus Medellín - Ciudad Universitaria",
    "Campus Medellín - Ciudadela Robledo",
    "Campus en el Área de la salud",
    "Campus Medellín - Sede de Posgrado",
    "Campus Medellín - Edificio San Ignacio",
    "Campus Medellín - Antigua Escuela de Derecho",
    "Campus Medellín - Edificio Antioquia",
    "Campus Medellín - Casas Patrimoniales",
    "Campus Medellín - Edificio de Extensión"
]

CANALES = [
    "Presencial",
    "Correo electrónico",
    "Página web",
    "Teléfono",
    "Redes sociales",
    "Otro"
]

CLASES = {
    "Petición": c_peticion,
    "Queja": c_queja,
    "Reclamo": c_reclamo,
    "Sugerencia": c_sugerencia
}


def pausar():
    """Pausa sencilla, cómoda y controlada."""

    input("\nPresione ENTER para continuar...")


def registrar_pqrs():
    """Registra una PQRS completa, validada y persistente."""

    print("\n" + "=" * 70)
    print("REGISTRAR PQRS")
    print("=" * 70)

    datos = solicitar_datos_solicitante()

    tipo = solicitar_opcion(
        "Tipo de solicitud",
        TIPOS
    )

    fecha = solicitar_fecha()

    momento_registro = datetime.now(ZoneInfo("America/Bogota"))
    fecha_registro = momento_registro.isoformat(timespec="seconds")
    hora_radicacion = momento_registro.strftime("%H:%M:%S")


    datos.update({

        "tipo_solicitud": tipo,

        "fecha_radicacion": fecha,
        "fecha_registro": fecha_registro,
        "hora_radicacion": hora_radicacion,

        "canal_recepcion": solicitar_opcion(
            "Canal de recepción",
            CANALES
        ),

        "asunto_titulo": solicitar_texto(
            "Asunto o título: ",
            5,
            150
        ),

        "descripcion_detallada": solicitar_descripcion(),

        "tipo_mascota": solicitar_opcion(
            "Tipo de mascota",
            ["Perro", "Gato"]
        ),

        "campus_relacionado": solicitar_opcion(
            "Campus relacionado",
            CAMPUS
        ),

        "fecha_maxima_respuesta":
            calcular_fecha_maxima(fecha),

        "estado_PQRS": "Registrada",

        "fecha_solucion": None
    })

    datos["id"] = obtener_siguiente_id(tipo)

    objeto = CLASES[tipo](datos)

    guardar_registro(objeto.datos)

    print(
        f"\nPQRS registrada correctamente."
        f" ID: {datos['id']}"
    )

    imprimir_radicado(datos)

    pausar()


def buscar_registro():
    """Busca un registro exacto por tipo e ID."""

    tipo = solicitar_opcion(
        "Seleccione el tipo de PQRS",
        TIPOS
    )

    entrada = input("Ingrese el ID: ").strip()

    if not entrada.isdigit():

        print("El ID debe ser numérico.")

        return None

    id_buscado = int(entrada)

    registros = leer_registros(tipo)

    for registro in registros:

        if registro["id"] == id_buscado:

            return registro

    print("No se encontró el registro.")

    return None


def consultar_pqrs():
    """Consulta las PQRS activas en orden de antigüedad."""

    registros = todos_los_registros()

    activas = [
        r for r in registros
        if r["estado_PQRS"] != "Solucionada"
    ]

    print("\n" + "=" * 70)
    print("CONSULTAR PQRS ACTIVAS")
    print("=" * 70)

    if not activas:

        print("No hay PQRS activas.")

    else:

        for r in sorted(
            activas,
            key=lambda x: x["fecha_radicacion"]
        ):

            print(
                f"ID: {r['id']} | "
                f"Tipo: {r['tipo_solicitud']} | "
                f"Nombre: {r['nombre_completo']} | "
                f"Estado: {r['estado_PQRS']} | "
                f"Vence: {r['fecha_maxima_respuesta']}"
            )

    pausar()


def cambiar_estado():
    """Actualiza el estado respetando el flujo establecido."""

    registro = buscar_registro()

    if not registro:

        pausar()

        return

    flujo = {

        "Registrada": ["En proceso"],

        "En proceso": ["Solucionada"],

        "Solucionada": []
    }

    actual = registro["estado_PQRS"]

    if not flujo[actual]:

        print("El registro ya está solucionado.")

        pausar()

        return

    nuevo = solicitar_opcion(
        f"Estado actual: {actual}",
        flujo[actual]
    )

    registro["estado_PQRS"] = nuevo

    if nuevo == "Solucionada":

        registro["fecha_solucion"] = date.today().isoformat()

    actualizar_registro(
        registro["tipo_solicitud"],
        registro["id"],
        registro
    )

    print("Estado actualizado correctamente.")

    pausar()


def imprimir_consulta():
    """Genera un radicado actualizado y exportable."""

    registro = buscar_registro()

    if registro:

        imprimir_radicado(registro)

    pausar()


def menu():
    """Menú principal, amigable, repetitivo y funcional."""

    preparar_archivos()

    while True:

        print("\n" + "=" * 70)
        print("VETERIPET-PQRS-UDEA")
        print("=" * 70)

        print("1. Registrar PQRS")
        print("2. Consultar PQRS")
        print("3. Registrar cambio en PQRS")
        print("4. Estadísticas")
        print("5. Imprimir radicado")
        print("6. Exportar estadísticas")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":

            registrar_pqrs()

        elif opcion == "2":

            consultar_pqrs()

        elif opcion == "3":

            cambiar_estado()

        elif opcion == "4":

            mostrar_estadisticas(
                todos_los_registros()
            )

            pausar()

        elif opcion == "5":

            imprimir_consulta()

        elif opcion == "6":
            exportar_estadisticas(todos_los_registros())

            pausar()

        elif opcion == "7":

            print(
                "\nGracias por utilizar "
                "VeteriPet-PQRS-Udea."
            )

            break

        else:

            print("Opción inválida.")


if __name__ == "__main__":

    menu()
