from initialSetting.datos_iniciales import obtener_color

def analizar_palabra(palabra,palabra_lista):
  """
  La funcion se encarga de leer letra por letra la palabra,y en su respectivo caso
  lo pinta del color correspondiente
  """
  lista_2=[]
  for i in range(len(palabra)):
    if palabra[i] in palabra_lista[i]:
      lista_2.append(obtener_color( palabra[i],"Verde" ))
    elif palabra[i] in palabra_lista:
      lista_2.append( obtener_color( palabra[i],"Amarillo" ))
    else:
      lista_2.append( obtener_color( palabra[i],"Rojo" )) 
  return lista_2