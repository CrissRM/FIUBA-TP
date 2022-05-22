from helpers.formatear_palabra import formatear_palabra


def validar_condicion_palabra():
  """
  Esta funcion es la encragrada de cumplir con la validacion de las condiciones para que la palabra
  sea valida,luego que termina con la validacion ,la devuelve en mayusculas
  """
  palabra=input("Arriesgo :")
  while len(palabra)!=5 or (not palabra.isalpha()):
    if len(palabra)!=5 :
        print(f"la palabra debe tener 5 letras y tiene {len(palabra)}")
    elif not palabra.isalpha() :
        print(f"La palabra debe contener solo letras")
    palabra=input("Arriesgo :") 
  palabra=formatear_palabra(palabra)
  """
  Aqui nos devuelve la palabra sin acentos,ver funcion especifica
  """
  return palabra.upper()
  