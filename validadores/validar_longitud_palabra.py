def validar_longitud_palabra():
  print("Palabra a adivinar: ? ? ? ? ?")
  palabra=input("Arriesgo: ")
  while len(palabra)!=5:
    print(f"La palabra debe tener 5 letras,usted ingreso una palabra de  '{len(palabra)}' letras")
    palabra=input("Ingrese una palabra nuevamente :") 
  return palabra

