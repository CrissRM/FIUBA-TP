from helpers.ingreso_de_jugadores import ingreso_de_jugadores
from modo_juego.inicial_juego import inicial_juego
from validadores.fin_juego import fin_juego

def inicia_app():
  jugadores = ingreso_de_jugadores()

  estadisticas_finales = inicial_juego(jugadores)
  
  fin_juego(estadisticas_finales)
  
  
inicia_app() 


  