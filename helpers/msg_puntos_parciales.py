def mensage(jugador_1,jugador_2,puntos_1,puntos_2,puntos_jugador_1,puntos_jugador_2):

  print("\n\x1b[33m*****************************PUNTAJES****************************\x1b[0m")
  print(f"\n\x1b[33m                    {'       JUGADOR      ':7} | {'PUNTOS':6} | {'ACOMULADO':9} |\x1b[0m")
  
    
  if puntos_jugador_1<0:
    print(f"\n                    {jugador_1:20} | {puntos_1:6} | \x1b[31m{puntos_jugador_1:9}\x1b[0m |")
  else:
    print(f"\n                    {jugador_1:20} | {puntos_1:6} | \x1b[32m{puntos_jugador_1:9}\x1b[0m |")
    
  if puntos_jugador_2<0:
    print(f"\n                    {jugador_2:20} | {puntos_2:6} | \x1b[31m{puntos_jugador_2:9}\x1b[0m |")
  else:
    print(f"\n                    {jugador_2:20} | {puntos_2:6} | \x1b[32m{puntos_jugador_2:9}\x1b[0m |")

def msg_puntos_parciales(jugador_1,jugador_2,puntos,parcial_ganador,turno,tiempo,puntos_jugador_1,puntos_jugador_2):

  if not parcial_ganador:
    puntos_1 = puntos
    puntos_2 = puntos + 50
    if turno ==1:
      mensage(jugador_1,jugador_2,puntos_1,puntos_2,puntos_jugador_1,puntos_jugador_2)
    else:
      puntos_1 = puntos+50
      puntos_2 = puntos 
      mensage(jugador_1,jugador_2,puntos_1,puntos_2,puntos_jugador_1,puntos_jugador_2)
  
  elif parcial_ganador == jugador_1:
    puntos_1 = -puntos
    puntos_2 = puntos 
    mensage(jugador_1,jugador_2,puntos_1,puntos_2,puntos_jugador_1,puntos_jugador_2)
    
  else:
    puntos_1 = puntos
    puntos_2 = -puntos 
    mensage(jugador_1,jugador_2,puntos_1,puntos_2,puntos_jugador_1,puntos_jugador_2)


