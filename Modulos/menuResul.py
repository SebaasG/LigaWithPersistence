# Author: mspg

import Modulos.utils as ut  # Importar utilidades para limpiar la consola
import Modulos.allMenu as all  # Importar los menús disponibles

# Diccionario global para almacenar los resultados de los partidos
resultados = {}

def menuResul(fechas: dict, equipos: dict):
    """
    Menú principal para la gestión de resultados.
    """
    isValid = True
    ut.limpiarConsola()
    try:
        while isValid:
            print(fechas)  # Mostrar fechas disponibles
            all.crearMenu(all.menuResul)  # Crear menú de opciones
            opc = int(input(": "))

            if opc == 1:
                regiResul(fechas, equipos)  # Registrar resultado
            elif opc == 2:
                verResultados()  # Ver resultados registrados
            elif opc == 3:
                mostrarEstadisticas(equipos)  # Mostrar estadísticas
                input("Presione cualquier tecla para continuar...")
            elif opc == 4:
                isValid = False  # Salir del menú
            else:
                print("Escogió un valor inválido")
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()

    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        input("Presione cualquier tecla para continuar...")
        ut.limpiarConsola()

def regiResul(fechas, equipos):
    """
    Registro del resultado de un partido.
    """
    if not fechas:
        print("No hay fechas disponibles.")
        input("Presione cualquier tecla para continuar...")
        return

    print("¿A qué encuentro le quiere registrar el resultado?")
    for index, fecha in enumerate(fechas.keys()):
        print(f"{index + 1}. {fecha}")
    
    try:
        opc = int(input(": ")) - 1
        if opc < 0 or opc >= len(fechas):
            print("Escogió un valor inválido.")
            input("Presione cualquier tecla para continuar...")
            return
        
        numFecha = list(fechas.keys())[opc]  # Seleccionar la fecha
        resultado(numFecha, equipos)  # Registrar el resultado

    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        input("Presione cualquier tecla para continuar...")

def resultado(numFecha, equipos):
    """
    Registra los goles para ambos equipos en la fecha seleccionada.
    """
    try:
        golesEq1 = int(input(f"¿Cuántos goles anotó el {equipos['01']['nombre']}?: "))
        golesEq2 = int(input(f"¿Cuántos goles anotó el {equipos['02']['nombre']}?: "))

        # Guardar resultado en el diccionario global
        resultados[numFecha] = {
            "equipo1": equipos['01']['nombre'],
            "golesEq1": golesEq1,
            "golesEq2": golesEq2,
            "equipo2": equipos['02']['nombre']
        }

        # Actualizar estadísticas de los equipos
        actualizar("01", golesEq1, golesEq2, equipos)
        actualizar("02", golesEq2, golesEq1, equipos)

        print(f"Resultado registrado para la fecha {numFecha}:")
        print(f"{equipos['01']['nombre']} {golesEq1} - {golesEq2} {equipos['02']['nombre']}")
        input("Presione cualquier tecla para continuar...")

    except ValueError:
        print("Error: Ingrese un número válido para los goles.")
        input("Presione cualquier tecla para continuar...")

def actualizar(idEquipo, golesFavor, golesContra, equipos):
    """
    Actualiza las estadísticas de un equipo tras registrar un partido.
    """
    equipos[idEquipo]['gf'] += golesFavor  # Goles a favor
    equipos[idEquipo]['gc'] += golesContra  # Goles en contra
    equipos[idEquipo]['pj'] += 1  # Partidos jugados

    if golesFavor > golesContra:
        equipos[idEquipo]['pg'] += 1  # Partidos ganados
        equipos[idEquipo]['pt'] += 3  # Puntos ganados
    elif golesFavor < golesContra:
        equipos[idEquipo]['pp'] += 1  # Partidos perdidos
    else:
        equipos[idEquipo]['pe'] += 1  # Partidos empatados
        equipos[idEquipo]['pt'] += 1  # Puntos por empate

    # Mostrar estadísticas actualizadas
    print(f"\nDatos actualizados de {equipos[idEquipo]['nombre']}:")
    for key, value in equipos[idEquipo].items():
        print(f"{key}: {value}")

def verResultados():
    """
    Mostrar todos los resultados registrados.
    """
    if not resultados:
        print("No hay resultados registrados.")
        input("Presione cualquier tecla para continuar...")
        return

    print("== Resultados Registrados ==")
    for fecha, resultado in resultados.items():
        print(f"Fecha: {fecha}")
        print(f"{resultado['equipo1']} {resultado['golesEq1']} - {resultado['golesEq2']} {resultado['equipo2']}")
        print("=============================")
    input("Presione cualquier tecla para continuar...")

def mostrarEstadisticas(equipos: dict):
    """
    Mostrar estadísticas del torneo.
    """
    if not equipos:
        print("No hay equipos registrados.")
        input("Presione cualquier tecla para continuar...")
        return

    # Cálculo de estadísticas
    equipoMasGoles = max(equipos.items(), key=lambda x: x[1]['gf'])
    equipoMasGc = max(equipos.items(), key=lambda x: x[1]['gc'])
    equipoUltimo = min(equipos.items(), key=lambda x: x[1]['pt'])

    # Mostrar estadísticas
    print("\n== Estadísticas del Torneo ==")
    print(f"Equipo con más goles marcados: {equipoMasGoles[1]['nombre']} ({equipoMasGoles[1]['gf']} goles)")
    print(f"Equipo con más goles en contra: {equipoMasGc[1]['nombre']} ({equipoMasGc[1]['gc']} goles)")
    print(f"Equipo en el último puesto: {equipoUltimo[1]['nombre']} ({equipoUltimo[1]['pt']} puntos)")

    input("Presione cualquier tecla para continuar...")
