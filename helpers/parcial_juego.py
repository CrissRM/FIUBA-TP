from helpers.contar_puntos import contar_puntos
from helpers.msg_puntos_parciales import msg_puntos_parciales
from helpers.formatear_tiempo import formatear_tiempo



def parcial_juego(jugador_1,jugador_2,contador_creditos,parcial_ganador,turno,inicia_juego,finaliza_juego):
  
  tiempo = formatear_tiempo(inicia_juego,finaliza_juego)
  
  puntos = contar_puntos(contador_creditos)
  
  msg_puntos_parciales(jugador_1,jugador_2,puntos,parcial_ganador,turno,tiempo,)

  res = input("¿ Desean seguir jugando ? (s/n): ") .lower()
  return res
  