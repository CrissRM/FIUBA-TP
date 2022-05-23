import doctest
letras = {
  "á": "a",
  "é": "e",
  "í": "i",
  "ó": "o",
  "ú": "u"
}

def formatear_palabra(palabra):
  """
    Esta funcion se encarga de transformar la palabra con acentos,a la misma sin acentos ,
    luego de verificar.
    Planteamos un dccionario con las vocales con acento como clave,y la letra sin acento como valor.
    Luego,llevamos la palabra a una lista para luego ver si las letras que 
    la componen tienen acentos ,en  caso de tenerlo ,lo busca en el diccionario 
    y lo reemplaza x su valor.
    Por ultimo junta las letras de la lista con un join

    >>> formatear_palabra("camío")
    'camio'

    >>> formatear_palabra("tildé")
    'tilde'

  """
  lista = [x for x in palabra]
  for i in range(len(lista)):
    if lista[i] in list(letras.keys()):
      lista[i] = letras[lista[i]]
  return "".join(lista)

import doctest
doctest.testmod()