def contabilizar_puntos(puntos,parcial_ganador,turno,puntos_jugador_1,puntos_jugador_2,jugador_1):
  """
  La funcion se encarga de analizar el reusltado del juego,y asignar sus valores,dependiendo
  del resultad y devolver los puntos acumulados en la jugada

  >>> contabilizar_puntos(10,"",1,0,10,"sebi")
  (60,20)
  correspondientes puntos del jugador 1 y 2,respectivamente

  """
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

import doctest
doctest.testmod()