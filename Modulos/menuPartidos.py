# Author: mspg

import Modulos.utils as ui
import Modulos.allMenu as all
from datetime import datetime

contador = 1  # Contador global para asignar ID a los encuentros

# Función principal del menú de partidos
def menuPartidos(equipos: dict, encuentros: dict):
    """
    Muestra el menú de partidos y gestiona la programación y visualización de partidos.
    """
    isValid = True
    try:
        while isValid:
            ui.limpiarConsola()
            all.crearMenu(all.menuPar)
            opc = input("Seleccione una opción: ")

            if opc.isdigit():
                opc = int(opc)
            else:
                print("Debe ingresar un número.")
                input("Presione cualquier tecla para continuar...")
                continue

            if opc == 1:
                ui.limpiarConsola()
                programar(equipos, encuentros)  # Llamada para programar un partido
                input("Presione una tecla para continuar...")
            elif opc == 2:
                ui.limpiarConsola()
                mostrarPartidos(encuentros)  # Llamada para mostrar partidos programados
                input("Presione una tecla para continuar...")
            elif opc == 3:
                isValid = False  # Finaliza el menú
                ui.limpiarConsola()
            else:
                print("Dato no válido, intente con otro.")
                input("Presione cualquier tecla para continuar...")
                ui.limpiarConsola()
    except ValueError as ve:
        print(f"Error en el sistema: {ve}")

    return encuentros

# Función para validar la fecha en formato correcto
def validarFecha(fecha_str: str) -> bool:
    formato = "%Y-%m-%d"
    try:
        fecha = datetime.strptime(fecha_str, formato)
        return True
    except ValueError:
        return False

# Función para programar partidos
def programar(equipos: dict, encuentros: dict):
    """
    Programa un partido entre dos equipos y guarda la información.
    """
    global contador
    nombresEquipos = [equipo["nombre"] for equipo in equipos.values()]

    # Selección del primer equipo
    print(f"Equipos disponibles: {nombresEquipos}")
    equipo1 = input("Ingrese el nombre del primer equipo: ")

    if equipo1 not in nombresEquipos:
        print("El equipo ingresado no está disponible.")
        return

    nombresEquipos.remove(equipo1)  # Eliminar el primer equipo para evitar duplicado

    # Selección del segundo equipo
    print(f"Equipos disponibles: {nombresEquipos}")
    equipo2 = input("Ingrese el nombre del segundo equipo: ")

    if equipo2 not in nombresEquipos:
        print("El equipo ingresado no está disponible.")
        return

    # Validación de fecha del partido
    fecha_valida = False
    while not fecha_valida:
        date = input("Ingrese la fecha del encuentro (formato AAAA-MM-DD): ")
        if validarFecha(date):
            fecha_valida = True
        else:
            print("Formato de fecha no válido. Intente nuevamente.")

    # Registro del encuentro en el diccionario de partidos
    encuentro = {
        "equipo1": equipo1,
        "equipo2": equipo2,
        "fecha": date
    }

    encuentros[str(contador).zfill(2)] = encuentro  # Asignar un ID único al partido
    contador += 1

def mostrarPartidos(encuentros):
    """
    Muestra todos los partidos programados hasta la fecha.
    """
    if not encuentros:
        print("No hay partidos programados.")
        return

    print("== Partidos Programados ==")
    for id_encuentro, datos in encuentros.items():
        equipo1 = datos["equipo1"]
        equipo2 = datos["equipo2"]
        fecha = datos["fecha"]

        # Mostrar la información de cada partido
        print(f"Partido {id_encuentro}:")
        print(f"{equipo1} vs {equipo2}")
        print(f"Fecha: {fecha}")
        print("==========================")

    print("Total de partidos programados:", len(encuentros))  # Mostrar el total de partidos programados
