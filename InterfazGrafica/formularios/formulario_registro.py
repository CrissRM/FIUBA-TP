from validadoresTk.validar_nombre import validar_nombre
from validadoresTk.validar_contrasenia import validar_contrasenia
from validadoresTk.existe_usuario import existe_usuario
from componentes.MsgBox import msg_warning,msg_error,msg_info
from componentes.Label import Label
from componentes.Entry import Entry
from componentes.Frame import Frame
from componentes.FrameHidden import FrameHidden
from componentes.Button import Button
from utils.grabar_datos import grabar_datos
from estilos_formatos import estilos,style_label,style_button,style_entry

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
        msg_info("Usuario registrado con éxito")
        nombre_entry.delete(0,"END")
        clave_entry.delete(0,"END")
        clave_entry_repeat.delete(0,"END")
        

    


def formulario_registro(root,btn_registro,btn_ingreso):
  form_registro = FrameHidden(root)
  
  #-----------------------------------------------------------------------------
  data_nombre = Frame(form_registro)
  style = style_label(data_nombre,"Nombre: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10)
  Label(style)

  nombre_entry = Entry(style_entry(data_nombre,0,0,"Releway",15,"normal","#fff","#000","left","?",15,"left",10,10,False))
  #-----------------------------------------------------------------------------
  data_clave = Frame(form_registro)
  style = style_label(data_clave,"Contraseña: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10)
  Label(style)
  clave_entry = Entry(style_entry(data_clave,0,0,"Releway",15,"normal","#fff","#000","left","?",15,"left",10,10,True))
  #-----------------------------------------------------------------------------
  data_clave_repeat =Frame(form_registro)
  style = style_label(data_clave_repeat,"Repetir Contraseña: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10)
  Label(style)
  clave_entry_repeat = Entry(style_entry(data_clave_repeat,0,0,"Releway",15,"normal","#fff","#000","left","?",15,"left",10,10,True))
  #-----------------------------------------------------------------------------
  
# --------------------------BOTONES OPCIONES--------------------------
  botones = Frame(form_registro)
  
  style = style_button(botones,"VOLVER",5,5,"Releway",10,"normal",10,"normal",volver,[form_registro,btn_ingreso,btn_registro],"back","left",10,10)
  Button(style)
  
  style = style_button(botones,"ENVIAR",5,5,"Releway",10,"normal",10,"normal",enviar,[nombre_entry,clave_entry,clave_entry_repeat],"send","left",10,10)
  Button(style)
  
  return form_registro