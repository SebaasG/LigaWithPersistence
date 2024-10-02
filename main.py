import Modulos.menu as index
import Modulos.menuEquipos as menuE
import Modulos.menuPlantel as menuP
import Modulos.menuPartidos as MenuPar
import Modulos.menuResul as menuRes
import Modulos.estadisticas as menuEstad

def main():
    equipos = {}
    jugadores = {}
    encuentros = {}
    activeMenu = True
    
    while activeMenu:
        res = index.crearMenu()  # Mostrar el menú principal
        
        if res == 1:
            try:
                menuE.subMenuEquipo(equipos)  # Acceder al submenú de equipos
            except ValueError:
                print("Ha ocurrido un error, intente más tarde.")
                
        elif res == 2:
            try:
                menuP.menuPlantel(equipos, jugadores)  # Acceder al menú del plantel
            except ValueError:
                print("Ocurrió un error al acceder al menú del plantel.")
                
        elif res == 3:
            encuentros = MenuPar.menuPartidos(equipos, encuentros)  # Programar partidos
        elif res == 4:
            res = menuRes.menuResul(encuentros, equipos)  # Acceder al menú de resultados
        
        elif res == 5:
            menuEstad.subMenuEquipo(jugadores)  # Acceder al menú de estadísticas
        elif res == 6:
            activeMenu = False 
    
if __name__ == "__main__":
    main()
