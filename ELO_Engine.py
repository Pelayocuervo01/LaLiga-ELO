# ELOnuevo = ELOactual + k (S - E)
# K-factor esta por verse cuanto pongo, de momento lo estandar es 16 para profesionales
# S resultado de la partida, 1 si gana, 0.5 por empate, 0 si pierde
# E se calcula asi:
# E = 1 / 1 + 10**(EloOponente - EloPersonal)/400
import math

def Elo_Engine(equipoLocal, equipoVisitante, ganador, equipoLocalElo, equipoVisitanteElo, diferencia_goles):
    
    k = 60

    # Ajuste por diferencia de goles
    factor_goles = math.log(diferencia_goles + 1) * 3.5 if diferencia_goles > 0 else 1

    # Expectativas
    ELocal = 1 / (1 + 10 ** ((equipoVisitanteElo - equipoLocalElo) / 400))
    EVisitante = 1 / (1 + 10 ** ((equipoLocalElo - equipoVisitanteElo) / 400))

    # Resultado del partido
    if ganador == equipoLocal:
        equipoLocalElo += k * (1 - ELocal) * factor_goles
        equipoVisitanteElo += k * (0 - EVisitante) * factor_goles
    elif ganador == equipoVisitante:
        equipoVisitanteElo += k * (1 - EVisitante) * factor_goles
        equipoLocalElo += k * (0 - ELocal) * factor_goles
    else:
        equipoLocalElo += k * (0.5 - ELocal)
        equipoVisitanteElo += k * (0.5 - EVisitante)

    return round(equipoLocalElo, 2), round(equipoVisitanteElo, 2)


print(Elo_Engine("Barsa", "Madrid", "burrito", 1200, 1204, 0))




