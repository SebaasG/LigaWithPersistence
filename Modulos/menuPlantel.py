# Author: mspg

import Modulos.utils as ui
import Modulos.allMenu as all

entrenadores = {}  # Diccionario para almacenar entrenadores
contador = 1  # Contador global para ID de jugadores y entrenadores

def menuPlantel(equipos: dict, jugadores: dict):
    """
    Muestra el menú del plantel y gestiona el registro de jugadores y entrenadores.
    """
    ui.limpiarConsola()
    isValid = True
    try:
        while isValid:
            all.crearMenu(all.menuPla)
            opc = int(input(": "))
            if opc == 1:
                validaEquipoDispo(equipos, 1, jugadores)  # Registrar jugador
            elif opc == 2:
                print(f"Sus jugadores son los siguientes: {jugadores}")  # Mostrar jugadores
            elif opc == 3:
                validaEquipoDispo(equipos, 2)  # Registrar entrenador
            elif opc == 4:
                print(f"Sus entrenadores son los siguientes: {entrenadores}")  # Mostrar entrenadores
            elif opc == 5:
                isValid = False  # Salir del menú
            else:
                print("Opción no válida, intente nuevamente.")
    except ValueError:
        print("Error en la ejecución del programa")

def registrarJugador(equipo: str, jugadores: dict):
    """
    Registra un nuevo jugador en el diccionario de jugadores.
    """
    global contador
    nom = str(input("Ingrese el nombre del jugador: "))
    dorsal = int(input("Ingrese el dorsal del jugador: "))
    pos = str(input("Ingrese la posición del jugador: "))
    
    jugador = {
        "nombre": nom,
        "dorsal": dorsal,
        "posicion": pos,
        "equipo": equipo,
        "golAn": 0,
        "tarjeAma": 0,
        "tarjeRoja": 0,
        "FalCome": 0
    }

    print(f"Se registró con éxito a: {jugador}")
    jugadores[str(contador).zfill(2)] = jugador
    contador += 1

def validaEquipoDispo(equipos: dict, num: int, jugadores=None):
    """
    Valida la disponibilidad del equipo para registrar jugadores o entrenadores.
    """
    try:
        info = [info["nombre"] for info in equipos.values()]
        print(info)

        nomEquipo = str(input(": "))
        if num == 1:
            registrarJugador(nomEquipo, jugadores)  # Registrar jugador
        elif num == 2:
            registrarEntrenador(nomEquipo)  # Registrar entrenador
        return nomEquipo
    except ValueError:
        print("Error en el sistema")

def registrarEntrenador(eq: str):
    """
    Registra un nuevo entrenador en el diccionario de entrenadores.
    """
    global contador
    print(f"Escoja qué rol, los disponibles son: \n")
    all.crearMenu(all.menuPlaRoll)
    rolEn = int(input(": "))
    nomEn = str(input(f"Nombre: "))

    nameRol = all.menuPlaRoll.get(rolEn, "Rol no encontrado")
    
    entrenador = {
        "nombre": nomEn,
        "rol": nameRol,
        "equipo": eq
    }
    
    entrenadores[str(contador).zfill(1)] = entrenador
    print(f"Se registró con éxito a: {entrenador}")
    contador += 1
