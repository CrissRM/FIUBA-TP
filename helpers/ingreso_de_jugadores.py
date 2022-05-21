import os

def ingreso_de_jugadores():
  os.system("cls")
  print("\n\n\x1b[33m********************* REGISTRO DE JUGADORES *********************\x1b[0m")
  print("\n\n\x1b[33m*****************************************************************\x1b[0m")
  jugador_1 = input("Por favor, ingrese el nombre del primer jugador: ")
  while not jugador_1.isalpha():
    print("\n\x1b[31m>>>> ALERTA!! Solo se aceptan caracteres alfabeticos...\x1b[0m")
    jugador_1 = input("Por favor, ingrese un nombre valido: ")
  print("\n\n\n\x1b[33m*****************************************************************\x1b[0m")
  jugador_2 = input("Por favor, ingrese el nombre del segundo jugador: ")
  while not jugador_2.isalpha():
    print("\n\x1b[31m>>>> ALERTA!! Solo se aceptan caracteres alfabeticos...\x1b[0m")
    jugador_2 = input("Por favor, ingrese un nombre valido: ")
      

  return [jugador_1,jugador_2]

