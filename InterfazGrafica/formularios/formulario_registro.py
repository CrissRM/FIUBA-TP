from componentes.Label import Label
from componentes.Entry import Entry
from componentes.Frame import Frame
from componentes.FrameHidden import FrameHidden
from componentes.Button import Button
from estilos_formatos import estilos,style_label,style_button,style_entry
from funcionalidadButtonTk.actions_button import volver,guardar


def formulario_registro(root,btn_registro,btn_ingreso):
  form_registro = FrameHidden(root)
  
  #-----------------------------------------------------------------------------
  data_nombre = Frame(form_registro)
  
  Label(style_label(data_nombre,"Nombre: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))

  nombre_entry = Entry(style_entry(data_nombre,0,0,"Releway",15,"normal","#fff","#000","left","?",15,"left",10,10,False))
  #-----------------------------------------------------------------------------
  data_clave = Frame(form_registro)

  Label(style_label(data_clave,"Contraseña: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))
  
  clave_entry = Entry(style_entry(data_clave,0,0,"Releway",15,"normal","#fff","#000","left","*",15,"left",10,10,True))
  #-----------------------------------------------------------------------------
  data_clave_repeat =Frame(form_registro)
  
  Label(style_label(data_clave_repeat,"Repetir Contraseña: ",5,5,"Releway",12,"roman",15,"w",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"left",10,10))
  
  clave_entry_repeat = Entry(style_entry(data_clave_repeat,0,0,"Releway",15,"normal","#fff","#000","left","*",15,"left",10,10,True))
  #-----------------------------------------------------------------------------
  
# --------------------------BOTONES OPCIONES--------------------------
  botones = Frame(form_registro)
  
  Button(style_button(botones,"VOLVER",5,5,"Releway",10,"normal",10,"normal",volver,[form_registro,btn_ingreso,btn_registro],"back","left",10,10))
  
  Button(style_button(botones,"GUARDAR",5,5,"Releway",10,"normal",10,"normal",guardar,[form_registro,btn_registro,btn_ingreso,nombre_entry,clave_entry,clave_entry_repeat],"send","left",10,10))
  
  return form_registro