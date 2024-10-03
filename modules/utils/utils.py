import os

def limpiarConsola():
    """Limpia la consola dependiendo del sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")

def validar(opc: int, dir: dict) -> bool:
    """
    Valida si la opción ingresada está en el diccionario proporcionado.
    Si no es válida, muestra un mensaje y limpia la consola.
    """
    if opc not in dir:
        print("Su opción no es válida, escoja otra.")
        input('Presione cualquier tecla para continuar...') 
        limpiarConsola()  
        return False 
    return True
