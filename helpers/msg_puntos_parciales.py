def msg_puntos_parciales(jugador_1,jugador_2,puntos,parcial_ganador,turno,tiempo):
  
  if not parcial_ganador:
    
    if turno ==1:
      print(f""" 
    {jugador_1} obtuvo ----> {puntos} puntos
    Puntos acomulados:  NO SE ME OCURRE COMO
    
    {jugador_2} obtuvo ----> {puntos+50} puntos
    Puntos acomulados:  NO SE ME OCURRE COMO
    
    """)
    else:
      print(f""" 
    {jugador_1} obtuvo ----> {puntos+50} puntos
    
    {jugador_2} obtuvo ----> {puntos} puntos
    
    """)

  elif parcial_ganador == jugador_1:
    
    print(f""" 
    {jugador_1} obtuvo ----> {puntos} puntos
    Puntos acomulados:  NO SE ME OCURRE COMO
    
    {jugador_2} obtuvo ----> {-puntos} puntos
    Puntos acomulados:  NO SE ME OCURRE COMO
    
    {tiempo} en adivinar la palabra
    """)
  else:
    
    print(f""" 
    {jugador_1} obtuvo ----> {-puntos} puntos
    Puntos acomulados:  NO SE ME OCURRE COMO
    
    {jugador_2} obtuvo ----> {puntos} puntos
    Puntos acomulados:  NO SE ME OCURRE COMO
    
    {tiempo} en adivinar la palabra
    """)