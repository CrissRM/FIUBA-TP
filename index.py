from initialSetting.datos_iniciales import condiciones_estandar
from validadores.fin_juego import fin_juego
from helpers.ingreso_de_jugadores import ingreso_de_jugadores
from helpers.parcial_juego import parcial_juego
from helpers.alternador_turnos import alternador_turnos
from helpers.contar_puntos import contar_puntos
from helpers.contabilizar_puntos import contabilizar_puntos
from app import app
import random
import os
import time


def inicia_app():
  jugador_1,jugador_2 = ingreso_de_jugadores()
  turno = random.randint(1,2)
  os.system("clear")
  
  puntos_jugador_1 = condiciones_estandar()["puntos_jugador_1"]
  puntos_jugador_2 = condiciones_estandar()["puntos_jugador_2"]

  res="s"
  while res =="s":
    
    inicia_juego = time.time()
    turno =alternador_turnos(turno)
    
    condiciones_iniciales = condiciones_estandar()
    condiciones_iniciales["jugador_1"] = jugador_1
    condiciones_iniciales["jugador_2"] = jugador_2
    condiciones_iniciales["turno"] = turno
        
  
    print(condiciones_iniciales["palabra_secret"])
    
    ronda_terminada = app(condiciones_iniciales)
    
    ronda_terminada["jugador_1"] = jugador_1
    ronda_terminada["jugador_2"] = jugador_2
    ronda_terminada["inicia_juego"] = inicia_juego
    
    contador_creditos = ronda_terminada["contador_credito"]
    parcial_ganador = ronda_terminada["parcial_ganador"]
    turno = ronda_terminada["turno"]
    
    puntos = contar_puntos(contador_creditos)

    puntos_jugador_1,puntos_jugador_2 = contabilizar_puntos(puntos,parcial_ganador,turno,puntos_jugador_1,puntos_jugador_2,jugador_1)

    res= parcial_juego(ronda_terminada,puntos_jugador_1,puntos_jugador_2)
    os.system("clear")
  
  fin_juego(puntos_jugador_1,puntos_jugador_2,jugador_1,jugador_2)
    

  

inicia_app()


  