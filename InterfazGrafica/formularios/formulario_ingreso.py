from validadoresTk.validar_nombre import validar_nombre
from validadoresTk.validar_contrasenia import validar_contrasenia
from componentes.FrameHidden import FrameHidden
from componentes.Frame import Frame
from componentes.Label import Label
from componentes.Entry import Entry
from componentes.Button import Button
from componentes.MsgBox import msg_warning
from estilos_formatos import estilos,style_label,style_button,style_entry


def volver(argumentos):
  form,btn_registro,btn_ingreso = argumentos
  form.pack_forget()
  btn_ingreso["state"] = "normal"
  btn_registro["state"] = "normal"

def enviar(argumentos):
  nombre_entry,clave_entry,jugadores,inicia_app,root = argumentos 
  nombre = nombre_entry.get()
  password = clave_entry.get()
  if nombre =="":
    msg_warning("El campo nombre es requerido")
  else:
    usuario_valido = validar_nombre(nombre)

  if password =="":
    msg_warning("El campo contraseña es requerido")
  else:
    password_valida = validar_contrasenia(password)
  
  if usuario_valido and password_valida:
    root.destroy()
    inicia_app()

def formulario_ingreso(root,btn_registro,btn_ingreso,jugadores,inicia_app):
  
  form_ingreso = FrameHidden(root)
  #-----------------------------------------------------------------------------
  data_nombre = Frame(form_ingreso)
  
  style = style_label(data_nombre,"Nombre: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10)
  Label(style)
  
  nombre_entry = Entry(style_entry(data_nombre,0,0,"Releway",15,"normal","#fff","#000","left","?",15,"left",10,10,False))
  #-----------------------------------------------------------------------------
  data_clave = Frame(form_ingreso)
  
  style = style_label(data_clave,"Contraseña: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10)
  Label(style)
  # style_entry(parent,padx,pady,font_family,font_size,font_slant,background,foreground,justify,show,side,mgx,mgy,is_password)
  clave_entry = Entry(style_entry(data_clave,0,0,"Releway",15,"normal","#fff","#000","left","?",15,"left",10,10,True))
  #-----------------------------------------------------------------------------
  botones = Frame(form_ingreso)

  style = style_button(botones,"VOLVER",5,5,"Releway",10,"normal",10,"normal",volver,[form_ingreso,btn_ingreso,btn_registro],"back","left",10,10)
  Button(style)

  style = style_button(botones,"ENVIAR",5,5,"Releway",10,"normal",10,"normal",enviar,[nombre_entry,clave_entry,jugadores,inicia_app,root],"send","left",10,10)
  Button(style)
  #----------------------------------------------------------------------------
  
  return form_ingreso
  