def alternador_turnos(turno):
  """
  Esta funcion se encarga de alternan los turnos para el uso de dos jugadores,en el caso de que sea
  igual a 1,juega un jugador y luego,ve el valor de turno para ver quien sigue.

  >>> alternador_turnos(1)
  2
  >>> alternador_turnos(2)
  1


  """
  if turno ==1:
    turno+=1
  else :
    turno-=1
  return turno
    

import doctest
doctest.testmod()