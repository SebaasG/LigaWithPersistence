# Author: mspg

import modules.allMenu as all
import modules.utils.utils as ut
import modules.utils.core as core
contador = 1  # Contador global para asignar ID a los equipos registrados
ligaRoute = 'data/torneo.json'
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
                equipos = core.ReadFile()
                # Opción para mostrar los equipos registrados
                ut.limpiarConsola()
                if not equipos.get('LigaBetplay').get('Equipos'):
                    print("Aún no se han registrado equipos.")
                else:

                    for key, value in equipos.get('LigaBetplay').get('Equipos').items():
                        print(f"ID: {key}, Nombre: {value.get('nombre')}")
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
    equipos = core.ReadFile()
    
    if not equipos.get('LigaBetplay', {}).get('Equipos'):
        contador = 1
    else:
       
        contador = len(equipos.get('LigaBetplay')['Equipos'].keys()) + 1
        print(contador)

    equipo = pedirDatos()  # Obtener datos del equipo
   
    eq[int(contador)] = equipo
    
    core.AddData(ligaRoute, {'LigaBetplay': {'Equipos': eq}})




def pedirDatos():
    """
    Solicita al usuario los datos del equipo y los devuelve en un diccionario.
    """
    name = input("Ingrese el nombre de su equipo: ").strip().lower()  # Pedir el nombre del equipo
    datos = {
        "nombre": name,
        "jugadores": {},
        "plantel": {},
        "pj": 0,  # Partidos jugados
        "pg": 0,  # Partidos ganados
        "pp": 0,  # Partidos perdidos
        "pe": 0,  # Partidos empatados
        "gf": 0,  # Goles a favor
        "gc": 0,  # Goles en contra
        "pt": 0,  # Puntos
    }
    return datos  # Retornar datos del equipo
