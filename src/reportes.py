
from datetime import date, datetime
from collections import Counter
from pathlib import Path


def promedio_dias_respuesta(registros):
    """Calcula el promedio entero de días de respuesta."""

    dias = []

    for registro in registros:

        if registro["estado_PQRS"] == "Solucionada":

            if registro.get("fecha_solucion") and registro.get("fecha_registro") :

                inicio = datetime.fromisoformat(
                    registro["fecha_registro"]
                ).date()

                fin = date.fromisoformat(
                    registro["fecha_solucion"]
                )

                dias.append(max(0, (fin - inicio).days))

    return round(sum(dias) / len(dias)) if dias else 0


def generar_estadisticas(registros):
    """Genera estadísticas relevantes mediante comprensiones de listas."""

    tipos = Counter(
        r["tipo_solicitud"] for r in registros
    )

    mascotas = Counter(
        r["tipo_mascota"] for r in registros
    )

    estados = Counter(
        r["estado_PQRS"] for r in registros
    )

    proximas = [
        r for r in registros
        if r["estado_PQRS"] != "Solucionada"
        and 0 <= (
            date.fromisoformat(r["fecha_maxima_respuesta"])
            - date.today()
        ).days <= 5
    ]

    antiguas = sorted(
        registros,
        key=lambda r: r["fecha_radicacion"]
    )[:5]

    return {
        "Cantidad por tipo": dict(tipos),

        "Cantidad por mascota": dict(mascotas),

        "Cantidad por estado": dict(estados),

        "Promedio entero de días de respuesta":
            promedio_dias_respuesta(registros),

        "PQRS próximas a vencer":
            len(proximas),

        "Cinco PQRS más antiguas":
            antiguas
    }


def mostrar_estadisticas(registros):
    """Muestra resultados estadísticos claros y organizados."""

    if not registros:
        print("\nNo existen registros.")
        return

    resultados = generar_estadisticas(registros)

    print("\n" + "=" * 70)
    print("ESTADÍSTICAS VETERIPET-PQRS-UDEA")
    print("=" * 70)

    for nombre, valor in resultados.items():

        if nombre == "Cinco PQRS más antiguas":

            print(f"\n{nombre}:")

            for r in valor:

                print(
                    f"ID {r['id']} | "
                    f"{r['tipo_solicitud']} | "
                    f"{r['fecha_radicacion']} | "
                    f"{r['estado_PQRS']}"
                )

        else:

            print(f"\n{nombre}: {valor}")

def exportar_estadisticas(registros):
    """Exporta las estadisticas a un archivo te texto"""

    if not registros:
        print("\nNo existen registros para exportar")
        return

    resultados= generar_estadisticas(registros)
    ruta = Path(__file__).resolve().parent.parent / "data" / "Estadisticas.txt"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", encoding="utf-8" ) as archivo:
        archivo.write("ESTADÍSTICAS VETERIPET-PQRS-UDEA\n")
        archivo.write("=" *70 + "\n")

        for nombre, valor in resultados.items():
            archivo.write(f"\n{nombre}:\n")

            if nombre == "Cinco PQRS más antiguas":

                for r in valor:
                    archivo.write(
                        f"ID {r['id']} | "
                        f"{r['tipo_solicitud']} | "
                        f"{r['fecha_radicacion']} | "
                        f"{r['estado_PQRS']}\n"
                    )

            else:
                archivo.write(f"{valor}\n")

    print(f"\nEstadísticas exportadas correctamente en {ruta}.")
