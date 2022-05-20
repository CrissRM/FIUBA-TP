from helpers.formatear_tiempo import formatear_tiempo
from helpers.contar_puntos import contar_puntos
from helpers.msgSuccess import msgSuccess
from helpers.msgfail import msgFail

def acomular_puntos(puntos):
  return puntos

def fin_juego(usuario_ganador,puntaje):
  print(f"El ganador es {usuario_ganador} con un total de {puntaje} puntos")
  
 

# es_ganador,palabra_lista,inicia_juego,finaliza_juego,contador_credito
# puntos= contar_puntos(contador_credito)
#   tiempo = formatear_tiempo(inicia_juego,finaliza_juego)
  
  
#   msgSuccess(tiempo,puntos) if es_ganador else msgFail(palabra_lista,puntos)
#   return input("Desea jugar otra partida ? (S/N)").lower()