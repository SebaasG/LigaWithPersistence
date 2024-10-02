# Author: mspg

import Modulos.allMenu as all
import Modulos.utils as ui

def crearMenu():
    """
    Función para crear el menú principal de la Liga Betplay.
    """
    valid = True
    while valid:
        try:
            # Mostrar encabezado del menú
            print("*****************************************************")
            print("****               LIGA BETPLAY                  ****")
            print("*****************************************************")
            all.crearMenu(all.menuP)  # Mostrar opciones del menú
            
            resul = int(input(":"))  # Capturar opción seleccionada
            
            # Validar que la opción ingresada exista en el menú
            if not ui.validar(resul, all.menuP):
                continue
            
            valid = False  # Finalizar el bucle si la opción es válida
        
        except ValueError as e:
            # Mensaje de error en caso de ingresar un dato no válido
            print(f"El dato no es válido: {e}")
            input('Presione cualquier tecla para continuar...')
            ui.limpiarConsola()  # Limpiar la consola después de cada intento
    
    return resul  # Devolver la opción seleccionada
