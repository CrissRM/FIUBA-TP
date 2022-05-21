from initialSetting.initial_tablero import initial_tablero
from initialSetting.initial_conditions import palabra_secreta

def condiciones_estandar():
  return {
    "tablero": initial_tablero(),
    "palabra_secret": palabra_secreta(),
    "es_ganador": False,
    "contador_credito": 0,
    "puntos_jugador_1": 0,
    "puntos_jugador_2": 0
  }

