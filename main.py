import modules.menu as index
import modules.menuEquipos as menuE
import modules.menuPlantel as menuP
import modules.menuPartidos as MenuPar
import modules.menuResul as menuRes
import modules.estadisticas as menuEstad
import modules.utils.core as core

def main():
    equipos = {}
    jugadores = {}
    encuentros = {}
    activeMenu = True
    #hola esto es un comentario
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
    




if(__name__ == "__main__"):
    
    torneo = {
        'LigaBetplay': {}
    }
    core.MY_DATABASE = 'data/torneo.json'
    core.checkFile(torneo)
    main()
    



    # camper= {

    #     'idx' : str(len(campus.get('campers'))+1).zfill(3),
    #     'nombre' : 'Camper 1'
    # }

    # campus.get('campers').update({camper['idx']: camper})
    # core.addData(campus)



    
