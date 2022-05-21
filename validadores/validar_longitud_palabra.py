from helpers.formatear_palabra import formatear_palabra

def validar_longitud_palabra():
  
  print("\nPalabra a adivinar: ? ? ? ? ?")
  palabra=input("Arriesgo: \n").lower()
  
  while len(palabra)!=5:
    print(f"\n\n\x1b[31m La palabra debe tener 5 letras,usted ingreso una palabra de  '{len(palabra)}' letras\x1b[0m")
    palabra=input("Ingrese una palabra nuevamente :") 
  
  return formatear_palabra(palabra)

