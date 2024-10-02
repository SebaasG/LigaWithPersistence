# Author: mspg

import Modulos.utils as ut
import Modulos.allMenu as all

contador = 1  # Contador global para asignar ID a los equipos registrados

def subMenuEquipo(equipos: dict):
    """
    Muestra el submenú de equipos y gestiona las opciones seleccionadas.
    """
    ut.limpiarConsola()
    isValid = True

    while isValid:
        all.crearMenu(all.menuEq)  # Mostrar menú de opciones relacionadas con equipos
        try:
            opc = int(input(": "))  # Capturar opción seleccionada

            if opc == 1:
                # Opción para registrar un equipo
                ut.limpiarConsola()
                regEquipo(equipos)
                print("Se ha registrado correctamente su equipo.")
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()

            elif opc == 2:
                # Opción para mostrar los equipos registrados
                ut.limpiarConsola()
                if not equipos:
                    print("Aún no se han registrado equipos.")
                else:
                    print("Los siguientes son los equipos registrados:\n")
                    print([a['nombre'] for a in equipos.values()])
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()

            elif opc == 3:
                isValid = False  # Finalizar el submenú y regresar
                ut.limpiarConsola()

            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError:
            print("Hubo un error en el proceso, intente nuevamente.")

def regEquipo(eq: dict):
    """
    Registra un nuevo equipo en el diccionario de equipos.
    """
    global contador
    equipo = pedirDatos()  # Obtener datos del equipo
    eq[str(contador).zfill(2)] = equipo  # Asignar ID al equipo
    contador += 1  # Incrementar contador para el próximo equipo

def pedirDatos():
    """
    Solicita al usuario los datos del equipo y los devuelve en un diccionario.
    """
    name = input("Ingrese el nombre de su equipo: ").strip().lower()  # Pedir el nombre del equipo
    datos = {
        "nombre": name,
        "pj": 0,  # Partidos jugados
        "pg": 0,  # Partidos ganados
        "pp": 0,  # Partidos perdidos
        "pe": 0,  # Partidos empatados
        "gf": 0,  # Goles a favor
        "gc": 0,  # Goles en contra
        "pt": 0,  # Puntos
    }
    return datos  # Retornar datos del equipo
