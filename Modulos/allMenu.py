# Author: mspg

# Menú principal del torneo
menuP = {
    1: "Equipos torneo",
    2: "Plantel equipos",
    3: "Programar partidos",
    4: "Resultado fecha",
    5: "Estadísticas",
    6: "Salir",
}

# Menú de gestión de equipos
menuEq = {
    1: "Registrar equipo",
    2: "Ver Equipos",
    3: "Volver",
}

# Menú para gestionar el plantel de equipos (jugadores y entrenadores)
menuPla = {
    1: "Registrar Jugadores",
    2: "Ver jugadores",
    3: "Registrar entrenador",
    4: "Ver entrenadores",
    5: "Volver"
}

# Menú para roles de entrenadores
menuPlaRoll = {
    1: "Técnico",
    2: "Asistente técnico",
    3: "Preparador físico",
    4: "Cuerpo médico"
}

# Menú para la programación de partidos
menuPar = {
    1: "Programar partido",
    2: "Ver partidos",
    3: "Volver"
}

# Menú para las estadísticas de los jugadores
menuEstad = {
    1: "Registrar estadística jugador",
    2: "Ver estadísticas de jugadores",
    3: "Jugador que más falta ha cometido",
    4: "Jugador con más tarjetas amarillas",
    5: "Volver"
}

# Menú para los resultados de los partidos
menuResul = {
    1: "Registrar resultados",
    2: "Ver resultados",
    3: "Estadísticas especiales",
    4: "Volver"
}

def crearMenu(dir: dict):
    """
    Función para mostrar cualquier menú basado en un diccionario.
    """
    for key, value in dir.items():
        print(f"{key}) {value}")
