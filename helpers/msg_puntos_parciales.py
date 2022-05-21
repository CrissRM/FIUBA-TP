def mensage(jugador_1,jugador_2,puntos_1,puntos_2,puntos_jugador_1,puntos_jugador_2):

  print("\n\x1b[33m*****************************PUNTAJES****************************\x1b[0m")
  print(f"\n          {jugador_1} obtuvo ----> {puntos_1} puntos")
    
  if puntos_jugador_1<0:
    print(f"          \x1b[31mPuntos acomulados:  {puntos_jugador_1}\x1b[0m\n") 
  else:
    print(f"          \x1b[32mPuntos acomulados:  {puntos_jugador_1}\x1b[0m\n")

  print(f"          {jugador_2} obtuvo ----> {puntos_2} puntos")
    
  if puntos_jugador_2<0:
    print(f"          \x1b[31mPuntos acomulados:  {puntos_jugador_2}\x1b[0m") 
  else:
    print(f"          \x1b[32mPuntos acomulados:  {puntos_jugador_2}\x1b[0m")

def msg_puntos_parciales(jugador_1,jugador_2,puntos,parcial_ganador,turno,tiempo,puntos_jugador_1,puntos_jugador_2):
# rojo: \x1b[31m
# verde: \x1b[32m
# \x1b[0m
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


