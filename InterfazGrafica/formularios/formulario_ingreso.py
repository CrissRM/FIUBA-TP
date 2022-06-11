from validadores.validar_nombre import validar_nombre
from validadores.validar_contrasenia import validar_contrasenia
from componentes.FrameForm import FrameForm
from componentes.Frame import Frame
from componentes.Label import Label
from componentes.Entry import Entry
from componentes.Button import Button
from componentes.MsgBox import msg_warning

def volver(argumentos):
  form,btn_registro,btn_ingreso = argumentos
  form.pack_forget()
  btn_ingreso["state"] = "normal"
  btn_registro["state"] = "normal"

def enviar(argumentos):
  nombre_entry,clave_entry = argumentos
  nombre = nombre_entry.get()
  password = clave_entry.get()
  if nombre =="":
    msg_warning("El campo nombre es requerido")
  else:
    validar_nombre(nombre)

  if password =="":
    msg_warning("El campo contraseña es requerido")
  else:
    validar_contrasenia(password)

def formulario_ingreso(root,btn_registro,btn_ingreso):
  
  form_ingreso = FrameForm(root)

  data_nombre = Frame(form_ingreso)
  
  style_label = {
    "root": data_nombre,
    "text": "Nombre: ",
    "padding_x": 5,
    "padding_y":5,
    "margin_x": 10,
    "margin_y": 10,
    "font_family": "Raleway",
    "font_size": 12,
    "font_slant": "roman",
    "side": "left",
    "width":15,
    "anchor": "w"
  }

  Label(style_label)
  nombre_entry = Entry(data_nombre)
  
  data_clave = Frame(form_ingreso)

  style_label["root"] = data_clave
  style_label["text"] = "Contraseña: "
  Label(style_label)

  clave_entry = Entry(data_clave,True)
  
  # --------------------------BOTONES OPCIONES--------------------------
  botones = Frame(form_ingreso)

  style_button = {
    "root": botones,
    "text": "VOLVER",
    "padding_x": 5,
    "padding_y":5,
    "margin_x": 10,
    "margin_y": 10,
    "button_style": "back",
    "font_family": "Raleway",
    "font_size": 10,
    "font_slant": "roman",
    "side": "left",
    "state": "normal",
    "command": lambda: volver([form_ingreso,btn_ingreso,btn_registro])
  }


  Button(style_button)

  style_button["text"]="ENVIAR"
  style_button["command"]=lambda: enviar([nombre_entry,clave_entry])
  style_button["button_style"] = "send"

  Button(style_button)
  #----------------------------------------------------------------------------
  
  return form_ingreso
  