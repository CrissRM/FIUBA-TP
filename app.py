from validadores.validar_condicion_palabra import validar_condicion_palabra 
from validadores.validar_palabra import validar_palabra
from validadores.analizar_palabra import analizar_palabra
from initialSetting.obtener_color import obtener_color
from helpers.alternador_turnos import alternador_turnos
import time

    
def app(dicc):
  print("\x1b[33m*****************************************************************\x1b[0m")
  print("\x1b[33m**************************JUEGO INICIADO*************************\x1b[0m")
  
  tablero = dicc["tablero"]
  palabra_secret = dicc["palabra_secret"]
  contador_credito = dicc["contador_credito"]
  es_ganador = dicc["es_ganador"]
  jugador_1 = dicc["jugador_1"]
  jugador_2 = dicc["jugador_2"]
  turno = dicc["turno"]
  
  while (not es_ganador) and (contador_credito< 5):
    
    turno= alternador_turnos(turno)
    print(f"\n\nTurno de ----> {jugador_1}") if turno == 1 else print(f"\n\nTurno de ----> {jugador_2}")
    
    parcial_ganador = False
    palabra = validar_condicion_palabra()
    
    if validar_palabra(palabra,palabra_secret):
      turno= alternador_turnos(turno)
      parcial_ganador = jugador_1 if turno == 1 else jugador_2
      es_ganador=True 
      tablero[contador_credito] = [obtener_color( letra,"Verde" ) for letra in palabra]
      finaliza_juego = time.time()
    
    else:
      lista_2 = analizar_palabra(palabra,palabra_secret)
      tablero[contador_credito]=lista_2 
    
    if not es_ganador:
      contador_credito+=1
    
    if contador_credito>=5:
      finaliza_juego = time.time()
    
    for i in range(5): 
      print(" ".join(tablero[i]))  

  return {
    "finaliza_juego": finaliza_juego,
    "contador_credito": contador_credito,
    "parcial_ganador": parcial_ganador,
    "turno": turno
  }

  