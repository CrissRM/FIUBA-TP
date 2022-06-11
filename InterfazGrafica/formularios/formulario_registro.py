from validadores.validar_nombre import validar_nombre
from validadores.validar_contrasenia import validar_contrasenia
from validadores.existe_usuario import existe_usuario
from componentes.MsgBox import msg_warning,msg_error
from componentes.Label import Label
from componentes.Entry import Entry
from componentes.Frame import Frame
from componentes.FrameForm import FrameForm
from componentes.Button import Button
from utils.grabar_datos import grabar_datos

def volver(argumentos):
  form,btn_registro,btn_ingreso = argumentos
  form.pack_forget()
  btn_ingreso["state"] = "normal"
  btn_registro["state"] = "normal"

def enviar(argumentos):
  nombre_entry,clave_entry,clave_entry_repeat = argumentos
  nombre = nombre_entry.get()
  password = clave_entry.get()
  password_repeat = clave_entry_repeat.get()
  if nombre =="" and password =="":
    msg_warning("Los camos nombre y contraseña son requeridos")
  elif nombre =="":
    msg_warning("El campo nombre es requerido")
  elif password =="":
    msg_warning("El campo contraseña es requerido")
  elif password !=password_repeat:
    msg_error("Las contraseñas no coinciden")
  else:
    if validar_nombre(nombre) and validar_contrasenia(password):
      if existe_usuario(nombre):
        msg_warning("El usuario ya existe")
      else:
        grabar_datos(nombre,password)
        

    


def formulario_registro(root,btn_registro,btn_ingreso):
  form_registro = FrameForm(root)
  
  data_nombre = Frame(form_registro)

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
  
  data_clave = Frame(form_registro)
  
  style_label["root"] =data_clave
  style_label["text"] = "Contraseña: "
  Label(style_label)
  clave_entry = Entry(data_clave,True)

  
  data_clave_repeat =Frame(form_registro)

  style_label["root"] = data_clave_repeat
  style_label["text"] = "Repetir Contraseña: "
  Label(style_label)
  
  clave_entry_repeat = Entry(data_clave_repeat,True)
  
# --------------------------BOTONES OPCIONES--------------------------
  botones = Frame(form_registro)
  
  style_btn = {
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
    "command": lambda: volver([form_registro,btn_ingreso,btn_registro])
  }
  
  Button(style_btn)
  
  style_btn["text"]="ENVIAR"
  style_btn["command"]=lambda: enviar([nombre_entry,clave_entry,clave_entry_repeat])
  style_btn["button_style"] = "send"
  
  Button(style_btn)
  
  return form_registro