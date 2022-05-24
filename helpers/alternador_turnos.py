from random import choice
def alternador_turnos(turno,jugadores):
  """
  Esta funcion se encarga de alternan los turnos para el uso de dos jugadores,elije de forma aletoria
  entre las opciones de jugadores,y le asigna el primer turno a el jugador seleccionado.Se espera que la
  funcion reciba en turno un string,y en jugadores una lista con el nombre del jugador;y que nos devuelva
  un string con el nombre del jugador que es elejido para jugar
  ATENCION:el funcionamient del doctest no es el esperado en ciertos casos debido a la funcion choice

  >>> alternador_turnos("Sebastian",["Sebastian","Omar"])
  'Omar'
  

  """
  if len(jugadores) >1:
    
    nueva_lista = [jugador for jugador in jugadores if jugador != turno]
    turno = choice(nueva_lista)
  else:
    turno = jugadores[0]
  return turno
    
    

import doctest
doctest.testmod()
