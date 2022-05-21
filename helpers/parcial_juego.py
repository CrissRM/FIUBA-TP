from helpers.contar_puntos import contar_puntos
from helpers.msg_puntos_parciales import msg_puntos_parciales
from helpers.formatear_tiempo import formatear_tiempo

def parcial_juego(ronda_terminada,puntos_jugador_1,puntos_jugador_2):

  jugador_1 = ronda_terminada["jugador_1"]
  jugador_2 = ronda_terminada["jugador_2"] 
  inicia_juego = ronda_terminada["inicia_juego"]
  finaliza_juego = ronda_terminada["finaliza_juego"]
  turno = ronda_terminada["turno"]
  parcial_ganador = ronda_terminada["parcial_ganador"]
  contador_creditos = ronda_terminada["contador_credito"]
  
  tiempo = formatear_tiempo(inicia_juego,finaliza_juego)
  
  puntos = contar_puntos(contador_creditos)
  
  msg_puntos_parciales(jugador_1,jugador_2,puntos,parcial_ganador,turno,tiempo,puntos_jugador_1,puntos_jugador_2)
  
  print("\n\n\x1b[33m*****************************************************************\x1b[0m")
  
  res = input("¿ Desean seguir jugando ? (s/n): ") .lower()
  while res !="s" and res !="n":
    print("\nDebe ingresar 's' o 'n'")
    res = input("¿ Desean seguir jugando ? (s/n): ") .lower()
  return res
  