from validadores.validar_condicion_palabra import validar_condicion_palabra 
from validadores.validar_palabra import validar_palabra
from validadores.analizar_palabra import analizar_palabra
from initialSetting.datos_iniciales import obtener_color
from helpers.alternador_turnos import alternador_turnos
from helpers.mensaje_turno_de import mensaje_turno_de
import time

    
def app(datos_iniciales):
  """"
  Hasta aqui ,la app se encarga de tomar lo datos con sus diferentes funciones ya carcterizadas,
  para comenzar con el juego,
  Hasta esta parte ,el programa se encrag de analizar si la palabra ingresada es la misma 
  que la que el programa elije de manera aleatoria,donde en el caso de que no sea valida,
  alterna con los jugadores  y utiliza un credito para seguir con el proximo jugador.
  
  """
  print("\x1b[33m*****************************************************************\x1b[0m")
  print("\x1b[33m**************************JUEGO INICIADO*************************\x1b[0m")
  
  tablero = datos_iniciales["tablero"]
  palabra_secret = datos_iniciales["palabra_secret"]
  contador_credito = datos_iniciales["contador_credito"]
  es_ganador = datos_iniciales["es_ganador"]
  jugadores = list(datos_iniciales["jugadores"].keys())
  turno = datos_iniciales["turno"]
  CREDITO_MAX = datos_iniciales["contador_credito_max"]
  CANTIDAD_LETRAS = datos_iniciales["cantidad_letras"]
 

  print(palabra_secret)
  while (not es_ganador) and (contador_credito< CREDITO_MAX):
    
    turno= alternador_turnos(turno,jugadores)
    mensaje_turno_de(turno)
    
    ganador_parcial = False
    
    palabra = validar_condicion_palabra()
    
    if validar_palabra(palabra,palabra_secret):
      es_ganador=True 
      ganador_parcial = turno
      # turno= alternador_turnos(turno,jugadores)
      tablero[contador_credito] = [obtener_color( letra,"Verde" ) for letra in palabra]
      finaliza_juego = time.time()
    
    else:
      lista_2 = analizar_palabra(palabra,palabra_secret)
      tablero[contador_credito]=lista_2
    
    if not es_ganador:
      contador_credito+=1
    
    if contador_credito>=CREDITO_MAX:
      finaliza_juego = time.time()
    
    for i in range(CANTIDAD_LETRAS): 
      print(" ".join(tablero[i]))  

  return {
    "finaliza_juego": finaliza_juego,
    "contador_credito": contador_credito,
    "ganador_parcial": ganador_parcial,
    "turno": turno,
    "cambiar_turno": alternador_turnos(turno,jugadores)
  }

