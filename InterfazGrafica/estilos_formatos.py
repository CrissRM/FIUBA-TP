estilos = {
  "BACKGROUND_PRIMARY": "#000000",
  "FOREGROUND_PRIMARY": "#ededed",
  "BACKGROUND_BUTTON_REGISTRO":"#287233",
  "FOREGROUND_BUTTON_REGISTRO":"#ffffff",
  "BACKGROUND_BUTTON_REGISTRO_ACTIVE":"#1e552d",
  "BACKGROUND_BUTTON_INGRESO":"#002f68",
  "FOREGROUND_BUTTON_INGRESO":"#ffffff",
  "BACKGROUND_BUTTON_INGRESO_ACTIVE":"#002653",
  "BACKGROUND_BUTTON_VOLVER": "#d81800",
  "FOREGROUND_BUTTON_VOLVER": "#ffffff",
  "BACKGROUND_BUTTON_ENVIAR": "#0300eb",
  "FOREGROUND_BUTTON_ENVIAR": "#ffffff",
  "FONT_FAMILY":"Raleway",
  "FONT_SIZE_TITLE":20,
  "FONT_SIZE_SUBTITLE":15,
  "FONT_SIZE_TEXT":13,
  "BORDER_GROOVE":"groove"
}

def button_style(style):
  if style == "back":
    estilo = ("#d81800","#ffffff","#881800")
  elif style =="send":
    estilo = ("#0300eb","#ffffff","#03008b")
  elif style == "register":
    estilo = ("#287233","#ffffff","#1e552d")
  elif style == "signin":
    estilo = ("#002f68","#ffffff","#002653")
  return estilo

