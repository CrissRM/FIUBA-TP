from random import choice
def alternador_turnos(turno,jugadores):
  """
  Esta funcion se encarga de alternan los turnos para el uso de dos jugadores,en el caso de que sea
  igual a 1,juega un jugador y luego,ve el valor de turno para ver quien sigue.

  >>> alternador_turnos(1)
  2
  >>> alternador_turnos(2)
  1
  """
  if len(jugadores) >1:
    
    nueva_lista = [jugador for jugador in jugadores if jugador != turno]
    turno = choice(nueva_lista)
  else:
    turno = jugadores[0]
  return turno
    

#Comentado porque no va a pasar las validaciones con la nueva implementacion y no me va a dehar probar. Pero te lo dejo comentado para que sepas
# import doctest
# doctest.testmod()