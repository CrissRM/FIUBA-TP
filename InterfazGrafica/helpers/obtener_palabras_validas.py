"""
def obtener_palabras_validas (CANTIDAD_LETRAS) :
  if CANTIDAD_LETRAS == 5:
    lista = ["abran","abria","acojo","actuo","aguda", "agudo", "algas","almas","alojo", "alojo", "altas ", "altos", "andes", "anima", "apodo", "arcos", "ardan","ardes", "arios", "azote", "bajas", "bajan", "bardo", "bates", "bayas", "bebes","besen", "besos", "botas", "bodas", "bondi", "bonos", "borre", "botan","botes","bruta", "cagas", "cajas", "callo", "calma", "campo", "canas", "capas", "caros","casan", "casas", "cazan", "cazas", "caida", "caido", "ceder", "cenas", "cepas","ceras", "cerdo", "cerco", "ceros", "cerro", "ciega", "ciego", "cines", "clava","clavo", "calvo", "cogen", "coger", "colas", "coles", "coman", "conos", "capas","capaz", "copos", "copas", "coral", "corra", "corre", "cosas", "coses", "croar","cruje", "cuida", "culta", "culto", "cunas", "curso","dagas", "datos", "debes","dedos", "densa", "dijes", "doman", "domar", "donan", "donas","dones","dote","dunas", "unas", "duros", "echas", "echan", "edita", "ellos", "emana", "emoji", "enoja", "enojo", "entes", "envio", "erizo","errar", "error", "espia", "euros", "evita", "evito", "falla", "falta", "fetos", "filas", "firme", "focos", "fosos", "frias", "fugas", "fumar", "gafas", "galas", "galos", "ganas", "gases", "gatos", "genes", "giras", "giros", "goles","gorra", "grave", "grite", "grito", "hielo", "heces", "habia", "hacen", "hacia", "hacha", "hecho", "hijas", "hilos", "hojas", "hugos", "ideas", "iglus", "islas", "india", "jefes", "jerga", "jodas", "jugos", "jamon", "kenia", "kodak","kayak", "lacra", "libro", "lados", "lagos", "lamen", "larga", "latas", "lazos",  "lejos", "lenta", "lento", "libre", "linda", "locas", "locos", "lomos","loros", "losas", "luces", "leche", "lucha", "luche", "magos", "malas", "males","malos", "mamas", "manca", "manco", "manos", "manda", "mapas", "marco", "mares", "matar", "mayas", "mazos", "mesas", "metas", "metes", "miles", "minas", "mirar", "mitos", "modas", "mojar", "modos", "mojan", "moles", "monas", "monos","monte", "moras", "moros", "mozas", "mocos", "mulas", "multa", "muros", "musas", "nabos", "nadar", "naves", "nazis", "nubes", "nudos", "nieve", "nunca","nacer", "necio", "necia", "obras", "odiar", "odios", "ollas", "ombus", "ondas","onzas", "opera", "orcas", "orden", "otras", "ovulo", "paces", "pajas", "palas", "palma", "palos", "panes", "parda", "parar", "pares", "pases", "patos","pecas", "peces", "penas", "pense", "perdi", "pesas", "pesca", "pesos", "pesas","peces", "pican", "pedir", "pisar", "pleno", "plena", "pocas", "pocos", "podar","poder", "podia", "ponen", "poner", "posee", "pozos", "pajar", "pujan"]
  elif CANTIDAD_LETRAS == 6:
    lista = ["abadia","abollo"]
  return lista

"""

from initialSetting.datos_iniciales import condiciones_iniciales


def obtener_palabras_validas():
  archivo = open("InterfazGrafica/archivos_palabras/palabras.csv")
  dicc_palabras_secretas = dict()
  palabra = archivo.readline().split(",")[0]

  while palabra !="":
    if len(palabra) == condiciones_iniciales()["cantidad_letras"]:
      dicc_palabras_secretas.setdefault(palabra)
    palabra = archivo.readline().split(",")[0]

  
  print(dicc_palabras_secretas)
  archivo.close()

obtener_palabras_validas()
