def contabilizar_puntos(puntos,parcial_ganador,turno,puntos_jugador_1,puntos_jugador_2,jugador_1):
  if not parcial_ganador:
    if turno ==1:
      puntos_jugador_1+=puntos+50
      puntos_jugador_2+=puntos
    else:
      puntos_jugador_1+=puntos
      puntos_jugador_2+=puntos+50
  
  elif parcial_ganador == jugador_1:
    puntos_jugador_1+=-puntos
    puntos_jugador_2+=puntos
  else:
    puntos_jugador_1+=puntos
    puntos_jugador_2+=-puntos
  
  return puntos_jugador_1,puntos_jugador_2