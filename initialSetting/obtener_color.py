colores = {"Verde" : "\x1b[32m",
            "Amarillo" : "\x1b[33m",
            "GrisOscuro" : "\x1b[90m",
             "Defecto" : "\x1b[39m" ,
             "Rojo" : "\x1b[31m",
             "ENDC": "\x1b[0m"
              }


def obtener_color(letra,color):
    return colores[color] + letra + colores["ENDC"]