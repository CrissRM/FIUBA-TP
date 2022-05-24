def contabilizar_puntos(puntos,ganador_parcial,turno,dicc_jugadores):
  """
  La funcion se encarga de analizar el reusltado del juego,y asignar sus valores,dependiendo
  del resultad y devolver los puntos acumulados en la jugada

  >>> contabilizar_puntos(10,"",1,0,10,"sebi")
  (60,20)
  correspondientes puntos del jugador 1 y 2,respectivamente

  """
  if not ganador_parcial:
    
    for key in dicc_jugadores:
      if key == turno:
        dicc_jugadores[key] += puntos 
      else:
        dicc_jugadores[key] += puntos+50
  
  else:
    
    for key in dicc_jugadores:
      if key == turno:
        dicc_jugadores[key] += puntos
      else:
        dicc_jugadores[key] += -puntos

  
  return dicc_jugadores

# import doctest
# doctest.testmod()