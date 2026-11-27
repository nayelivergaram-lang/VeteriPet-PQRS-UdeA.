
import re
from datetime import datetime, date, timedelta


def solicitar_texto(mensaje, minimo=1, maximo=None, obligatorio=True):
    """Texto limpio, claro, seguro y validado."""

    while True:
        valor = input(mensaje).strip()

        if not valor and not obligatorio:
            return ""

        if not valor:
            print("El campo es obligatorio.")
            continue

        if len(valor) < minimo:
            print(f"Debe tener mínimo {minimo} caracteres.")
            continue

        if maximo is not None and len(valor) > maximo:
            print(f"Debe tener máximo {maximo} caracteres.")
            continue

        return valor


def solicitar_nombre():
    """Nombre completo, alfabético, correcto y obligatorio."""

    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+(?:[ '-][A-Za-zÁÉÍÓÚáéíóúÑñÜü]+)+$"

    while True:
        nombre = solicitar_texto("Nombre completo: ", 3, 100)

        if re.fullmatch(patron, nombre):
            return nombre

        print("Use letras y escriba nombre y apellido.")


def solicitar_opcion(mensaje, opciones):
    """Menú numerado, sencillo, amigable y controlado."""

    while True:
        print(f"\n{mensaje}")

        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")

        entrada = input("Seleccione una opción: ").strip()

        if entrada.isdigit() and 1 <= int(entrada) <= len(opciones):
            return opciones[int(entrada) - 1]

        print("Opción inválida.")


def solicitar_documento():
    """Documento numérico, obligatorio y validado."""

    while True:
        numero = input("Número de documento: ").strip()

        if numero.isdigit() and 3 <= len(numero) <= 15:
            return numero

        print("Debe contener entre 3 y 15 dígitos.")


def solicitar_telefono():
    """Teléfono numérico, obligatorio y de diez dígitos."""

    while True:
        telefono = input("Teléfono de contacto: ").strip()

        if telefono.isdigit() and len(telefono) == 10:
            return telefono

        print("Debe contener exactamente 10 dígitos.")


def solicitar_correo():
    """Correo electrónico válido, estructurado y obligatorio."""

    patron = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    while True:
        correo = input("Correo electrónico: ").strip()

        if len(correo) <= 254 and re.fullmatch(patron, correo):
            return correo

        print("Ingrese un correo válido.")


def solicitar_fecha():
    """Fecha válida, actual o pasada, nunca futura."""

    while True:
        texto = input("Fecha de radicación (DD/MM/AAAA): ").strip()

        try:
            fecha = datetime.strptime(texto, "%d/%m/%Y").date()

            if fecha <= date.today():
                return fecha.isoformat()

            print("La fecha no puede ser futura.")

        except ValueError:
            print("Formato inválido. Use DD/MM/AAAA.")


def calcular_fecha_maxima(fecha):
    """Fecha máxima automática, exacta y calculada a 30 días."""

    fecha = date.fromisoformat(fecha)

    return (fecha + timedelta(days=30)).isoformat()


def solicitar_descripcion():
    """Descripción amplia, detallada y obligatoria."""

    return solicitar_texto(
        "Descripción detallada: ",
        minimo=20,
        maximo=2000
    )


def solicitar_datos_solicitante():
    """Datos completos, ordenados y validados."""

    return {
        "nombre_completo": solicitar_nombre(),

        "tipo_documento": solicitar_opcion(
            "Tipo de documento",
            ["CC", "TI", "CE", "PP", "NIT"]
        ),

        "numero_documento": solicitar_documento(),

        "tipo_telefono": solicitar_opcion(
            "Tipo de teléfono",
            ["Celular", "Fijo", "Corporativo", "Otro"]
        ),

        "telefono_contacto": solicitar_telefono(),

        "correo_electronico": solicitar_correo(),

        "direccion": solicitar_texto(
            "Dirección (opcional): ",
            minimo=5,
            maximo=200,
            obligatorio=False
        )
    }
