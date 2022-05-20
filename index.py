from initialSetting.initial_tablero import initial_tablero
from initialSetting.initial_conditions import palabra_secreta
from validadores.fin_juego import fin_juego
from app import app
import time
from helpers.ingreso_de_jugadores import ingreso_de_jugadores
import random
from helpers.parcial_juego import parcial_juego

def inicia_app():
  [jugador_1,jugador_2] = ingreso_de_jugadores()
  turno = random.randint(1,2)
  res="si"
  while res == "si" or res =="s":
    

    inicia_juego = time.time()
    
    tablero = initial_tablero()
    
    palabra_lista=palabra_secreta()
    
    print(palabra_lista)
    
    es_ganador=False
    
    contador_credito=0

    [es_ganador,palabra_lista,finaliza_juego,contador_credito,parcial_ganador,turno] = app(tablero,palabra_lista,contador_credito,es_ganador,jugador_1,jugador_2,turno)
    

    res = parcial_juego(jugador_1,jugador_2,contador_credito,parcial_ganador,turno,inicia_juego,finaliza_juego)
    

  fin_juego("deberia terminar con acomular los puntos"," ")

inicia_app()