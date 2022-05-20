from validadores.validar_longitud_palabra import validar_longitud_palabra 
from validadores.validar_palabra import validar_palabra
from validadores.analizar_palabra import analizar_palabra
from initialSetting.obtener_color import obtener_color
import time
from helpers.alternador_turnos import alternador_turnos


def app(tablero,palabra_lista,contador_credito,es_ganador,jugador_1,jugador_2,turno):
  
  while (not es_ganador) and (contador_credito< 5):
    
    turno= alternador_turnos(turno)
    print(f"Turno de ----> {jugador_1}") if turno == 1 else print(f"Turno de ----> {jugador_2}")
    parcial_ganador = False
    palabra = validar_longitud_palabra()
    
    if validar_palabra(palabra,palabra_lista):
      parcial_ganador = jugador_1 if turno == 1 else jugador_2
      es_ganador=True 
      tablero[contador_credito] = [obtener_color( letra,"Verde" ) for letra in palabra]
      finaliza_juego = time.time()
    
    else:
      lista_2 = analizar_palabra(palabra,palabra_lista)
      tablero[contador_credito]=lista_2 
    
    if not es_ganador:
      contador_credito+=1
    
    if contador_credito>=5:
      finaliza_juego = time.time()
    
    for i in range(5): 
      print(" ".join(tablero[i]))  

  return [es_ganador,palabra_lista,finaliza_juego,contador_credito,parcial_ganador,turno]

  