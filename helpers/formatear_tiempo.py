import math
def formatear_tiempo(inicia,finaliza):
  time = math.floor(finaliza-inicia)
  horas=math.floor(time/3600)
  minutos= math.floor((time-horas*3600)/60)
  segundos= math.floor((((time-horas*3600)/60)-minutos)*60)

  return f"{horas} horas {minutos} minutos {segundos} segundos" if horas != 0 else f"{minutos} minutos {segundos} segundos"

  