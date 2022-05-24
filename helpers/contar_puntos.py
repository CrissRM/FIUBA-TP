def contar_puntos(contador_credito):
  """
  La funcion de esta parte del codigo,es determinar la cantidad de puntos correspondientes
  a la cantidad de intentos realizados.
  La fucnion recibe un numero entero y devuelve los puntos en numero entero

  >>> contar_puntos(0)
  50
  >>> contar_puntos(1)
  40
  >>> contar_puntos(5)
  -100

  """
  
  if contador_credito == 0:
    puntos=50
  elif contador_credito==1:
    puntos =40
  elif contador_credito==2:
    puntos =30
  elif contador_credito==3:
    puntos =20
  elif contador_credito==4:
    puntos =10
  else:
    puntos = -100
  return puntos



import doctest
doctest.testmod()