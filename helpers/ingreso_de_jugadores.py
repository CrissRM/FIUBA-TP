import os

def ingreso_de_jugadores():
  os.system("cls")
  print("\n\n\x1b[33m********************* REGISTRO DE JUGADORES *********************\x1b[0m")
  print("\n\n\x1b[33m*****************************************************************\x1b[0m")
  jugador_1 = input("Por favor, ingrese el nombre del primer jugador: ")
  while not (x.isalpha() or x.isspace() for x in jugador_1):
    """
    recorre letra por letra de mi jugador,si no es letra o no es espacio,pide nuevo nombre valido
    """
    print("\n\x1b[31m>>>> ALERTA!! Solo se aceptan caracteres alfabeticos...\x1b[0m")
    jugador_1 = input("Por favor, ingrese un nombre valido: ")
  print("\n\n\n\x1b[33m*****************************************************************\x1b[0m")
  jugador_2 = input("Por favor, ingrese el nombre del segundo jugador: ")
  while not (x.isalpha() or x.isspace() for x in jugador_2):
    print("\n\x1b[31m>>>> ALERTA!! Solo se aceptan caracteres alfabeticos...\x1b[0m")
    jugador_2 = input("Por favor, ingrese un nombre valido: ")
  palabra_jug_1=jugador_1.split(" ")
  for elementos in range(len(palabra_jug_1)):
      palabra_jug_1[elementos]=palabra_jug_1[elementos].capitalize()
  """
  Separa las palabras en lista,reemplaza las mismas con un inicio de mayuscula y devuelve unidas con espacio
  """
  palabra_jug_2=jugador_2.split(" ")
  for elementos in range(len(palabra_jug_2)):
      palabra_jug_2[elementos]=palabra_jug_2[elementos].capitalize()
  
  return [" ".join(palabra_jug_1)," ".join(palabra_jug_2)]

