def formatear_nombre(nombre):
  """
 
  La funcion recibe un nombre en forma de string y nos devuelve una tupla compuesta 
  por un check para verificar su condicion dpara ser una palabra valida ,y un string con el nombre
  con separada por espacios y con mayuscula en cada una de las letras que empiezan una palabra
  >>> formatear_nombre("el grupo serpiente es el mejor")
  (True, 'El Grupo Serpiente Es El Mejor')
  >>> formatear_nombre("equipo verde")
  (True,'Equipo Verde')
  """
  check = False
  array_name = [name.capitalize() for name in nombre.split()]
  i=0
  while i<len(array_name) and array_name[i].isalpha():
    i+=1
  if i == len(array_name):
    check = True
  
  return check," ".join(array_name)


import doctest
doctest.testmod()