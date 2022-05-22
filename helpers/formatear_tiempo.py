import math
def formatear_tiempo(inicia,finaliza):
  """
  Esta funcion es la encargada de contar el tiempo que conlleva desde el inicio al fin del juego.

  >>> formatear_tiempo(0,2100)
  '35 minutos 0 segundos'

  >>> formatear_tiempo(0,312312)
  '86 horas 45 minutos 12 segundos'
  
  """
  time = math.floor(finaliza-inicia)
  horas=math.floor(time/3600)
  minutos= math.floor((time-horas*3600)/60)
  segundos= math.floor((((time-horas*3600)/60)-minutos)*60)

  return f"{horas} horas {minutos} minutos {segundos} segundos" if horas != 0 else f"{minutos} minutos {segundos} segundos"



import doctest
doctest.testmod()