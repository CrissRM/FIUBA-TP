def fin_juego(puntos_jugador_1,puntos_jugador_2,jugador_1,jugador_2):
  print("*****************************************************************")
  print("**************************FIN DEL JUEGO*************************")
  if puntos_jugador_1>puntos_jugador_2:
    print(f"     GANADOR: {jugador_1} OBTUVO {puntos_jugador_1} PUNTOS")
  elif puntos_jugador_1<puntos_jugador_2:
    print(f"     GANADOR: {jugador_2} OBTUVO {puntos_jugador_2} PUNTOS")
  else:
    print(f"     ¡¡¡ EMPATE !!!")
  
