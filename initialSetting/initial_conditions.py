from unicodedata import numeric
from initialSetting.obtener_palabra import obtener_palabras_validas
import random

def num_random():
  return random.randint(0,len(obtener_palabras_validas()))

def palabra_secreta():
  palabra_secre = obtener_palabras_validas()
  palabra_secreta=palabra_secre[num_random()]
  return palabra_secreta



