# Author: mspg

import Modulos.utils as ut
import Modulos.allMenu as all

contador = 1  # Contador global para la función

def subMenuEquipo(jugadores: dict):
    """
    Menú para gestionar las estadísticas de los jugadores.
    """
    ut.limpiarConsola()
    isValid = True

    while isValid:
        all.crearMenu(all.menuEstad)  # Mostrar el menú de estadísticas
        try:
            opc = int(input(": "))
            if opc == 1:
                ut.limpiarConsola()
                regEstadistica(jugadores)  # Registrar estadísticas de un jugador
                print("Se ha registrado correctamente las estadísticas.")
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()
            elif opc == 2:
                ut.limpiarConsola()
                mostrarJugador(jugadores)  # Mostrar las estadísticas de todos los jugadores
                input("Presione una tecla para continuar")
            elif opc == 3:
                opc = faltasMax(jugadores)  # Mostrar jugador con más faltas
                print(opc)
                input("Presione una tecla para continuar...")
            elif opc == 4:
                opc = tarjetasMax(jugadores)  # Mostrar jugador con más tarjetas
                print(opc)
                input("Presione una tecla para continuar...")
            elif opc == 5:
                isValid = False  # Salir del menú
                ut.limpiarConsola()
            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError:
            print("Hubo un error en el proceso, intente nuevamente.")

def regEstadistica(jugadores: dict):
    """
    Función para registrar las estadísticas de un jugador.
    """
    print("Escoja a qué jugador le va a registrar las estadísticas: ")
    for idJugador, datosJugador in jugadores.items():
        print(f"ID: {idJugador}, Nombre: {datosJugador['nombre']}, Equipo: {datosJugador['equipo']}")
    
    opc = input(": ").zfill(2)  # Formato de ID de 2 dígitos
    
    if opc in jugadores:
        goles = input("Ingrese goles anotados: ")
        tarAmar = input("Ingrese tarjetas amarillas: ")
        tarRoja = input("Ingrese tarjetas rojas: ")
        falcom = input("Ingrese faltas cometidas: ")
        
        # Actualizar las estadísticas del jugador
        jugadores[opc]['golAn'] = int(goles)
        jugadores[opc]['tarjeAma'] = int(tarAmar)
        jugadores[opc]['tarjeRoja'] = int(tarRoja)
        jugadores[opc]['FalCome'] = int(falcom)
    else:
        print("No disponible en la lista")

def mostrarJugador(jugadores: dict):
    """
    Función para mostrar las estadísticas de todos los jugadores.
    """
    for idJugador, datosJugador in jugadores.items():
        print(f"ID: {idJugador}")
        print(f"Nombre: {datosJugador['nombre']}")
        print(f"Equipo: {datosJugador['equipo']}")
        print(f"Dorsal: {datosJugador['dorsal']}")
        print(f"Posición: {datosJugador['posicion']}")
        print(f"Goles anotados: {datosJugador['golAn']}")
        print(f"Tarjetas amarillas: {datosJugador['tarjeAma']}")
        print(f"Tarjetas rojas: {datosJugador['tarjeRoja']}")
        print(f"Faltas cometidas: {datosJugador['FalCome']}")
        print("-" * 30)  # Separador visual

def faltasMax(jugadores: dict):
    """
    Función para obtener el jugador con más faltas cometidas.
    """
    jugadorMax = None
    maxFaltas = -1

    for jugador in jugadores.values():
        if jugador['FalCome'] > maxFaltas:
            maxFaltas = jugador['FalCome']
            jugadorMax = jugador

    return jugadorMax

def tarjetasMax(jugadores: dict):
    """
    Función para obtener el jugador con más tarjetas (amarillas + rojas).
    """
    jugadorMax = None
    maxTarjetas = -1

    for jugador in jugadores.values():
        totalTarjetas = jugador['tarjeAma'] + jugador['tarjeRoja']
        if totalTarjetas > maxTarjetas:
            maxTarjetas = totalTarjetas
            jugadorMax = jugador

    return jugadorMax
