from helpers.formatear_tiempo import formatear_tiempo

def mensaje_para_usurio(dicc_jugadores,puntos_ronda,ronda_terminada):
  """
  Recibe por parametro diccionario con los jugadores y sus respectivos puntos como valores,los puntos
  que se obtuvieron en la ronda y cuando la ronda finaliza en forma de su respectivo tiempo que 
  conllevo la ronda
  Mostrara por pantalla los datos obtenidos de la ronda
  """
  
  print("\n\x1b[33m*****************************PUNTAJES****************************\x1b[0m")
  
  print(f"\n\x1b[33m                    {'       JUGADOR      ':7} | {'PUNTOS':6} | {'ACOMULADO':9} |\x1b[0m")
  
  if ronda_terminada["ganador_parcial"]:
    for jugador,puntos in dicc_jugadores.items():
      if puntos<0:
        if ronda_terminada["ganador_parcial"] == jugador:
          print(f"\n                    {jugador:20} | {puntos_ronda:6} | \x1b[31m{puntos:9}\x1b[0m |")
        else:
          print(f"\n                    {jugador:20} | {-puntos_ronda:6} | \x1b[31m{puntos:9}\x1b[0m |")
      else:
        if ronda_terminada["ganador_parcial"] == jugador:
          print(f"\n                    {jugador:20} | {puntos_ronda:6} | \x1b[32m{puntos:9}\x1b[0m |")
        else:
          print(f"\n                    {jugador:20} | {-puntos_ronda:6} | \x1b[32m{puntos:9}\x1b[0m |")
    
    
    print(f"\n          Tiempo en adiviniar la palabra: {formatear_tiempo(ronda_terminada)}") 

  else:
    for jugador,puntos in dicc_jugadores.items():
      if puntos<0:
        if ronda_terminada["turno"] == jugador:
          print(f"\n                    {jugador:20} | {puntos_ronda:6} | \x1b[31m{puntos:9}\x1b[0m |")
        else: 
          print(f"\n                    {jugador:20} | {puntos_ronda+50:6} | \x1b[31m{puntos:9}\x1b[0m |")
      else:
        if ronda_terminada["turno"] == jugador:
          print(f"\n                    {jugador:20} | {puntos_ronda:6} | \x1b[32m{puntos:9}\x1b[0m |")
        else:
          print(f"\n                    {jugador:20} | {puntos_ronda+50:6} | \x1b[31m{puntos:9}\x1b[0m |")


