def contabilizar_puntos(puntos,ganador_parcial,turno,dicc_jugadores):
  """
  La funcion se encarga de analizar el resultado del juego,y asignar sus valores,dependiendo
  del resultad y devolver los puntos acumulados en la jugada.
  La funcion recibira un numero entero en puntos,luego el nombre del jugador ganador o False en caso de 
  que no exista un ganador,el nombre del jugador del turno ,y un diccionario que tendra como clave el nombre
  del jugador y como valor los puntos del mismo.
  Nos devuelve un diccionario con el nombre de los jugadores y los puntos finales

  >>> contabilizar_puntos(10,False,"Juan",{"Juan":30,"Alan":20})
  {'Juan': 40, 'Alan': 80}
  
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

import doctest
doctest.testmod()