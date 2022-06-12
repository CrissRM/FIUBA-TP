import tkinter as tk
from componentes.MsgBox import msg_error, msg_info, msg_warning
from componentes.FrameHidden import FrameHidden
from utils.estilos_formatos import estilos
from formularios.formulario_registro import formulario_registro
from formularios.formulario_ingreso import formulario_ingreso
from componentes.Label import Label
from componentes.Button import Button
from componentes.Frame import Frame
from componentes.Entry import Entry
from app.app_consola import inicia_app
from estilos_formatos import estilos,style_label,style_button,style_entry


def btn_registrarse(not_argument):
  form_registro = formulario_registro(root,registro,ingresar)
  form_registro.pack()
  registro["state"] = "disabled"
  ingresar["state"] = "disabled"
  
def btn_ingresar(not_argument):
  cant_jugadores.pack()
  registro["state"] = "disabled"
  ingresar["state"] = "disabled"

def handler_cant(not_argument):
  try:
    cant = int(cant_entry.get())
  except ValueError:
    msg_error("No es valido. Ingresar números enteros")
  else:
    if cant <= 0:
      msg_warning("No es un valor, válido")
    elif cant<=2:
      jugadores = dict()
      cant_jugadores.pack_forget()
      form_ingreso = formulario_ingreso(root,registro,ingresar,jugadores,inicia_app)
      form_ingreso.pack()
    else:
      msg_info("Por el momento, el juego está implementado para un máximo de 2 jugadores")

root = tk.Tk()
root.title("FIUBLE - SERPIENTE")
root.geometry("+300+200")
root.minsize(width=700,height=400)
root.configure(background=estilos["BACKGROUND_PRIMARY"])

#------------------------------------TITULO------------------------------------
Label(style_label(root,"FIUBELE-SERPIENTE",5,5,"Releway",25,"roman",25,"center",estilos["BACKGROUND_PRIMARY"],estilos["FOREGROUND_PRIMARY"],"top",10,10))
#-------------------------------------------------------------------------------


#---------------------------FRAME CANTIDAD JUGADORES---------------------------
cant_jugadores = FrameHidden(root)

# style_entry(parent,padx,pady,font_family,font_size,font_slant,background,foreground,justify,show,side,mgx,mgy,is_password)
cant_entry = Entry(style_entry(cant_jugadores,10,10,"Releway",13,"normal","#fff","#000","left","?",3,"left",10,0,False))

Button(style_button(cant_jugadores,"CONFIRMAR",3,3,"Releway",8,"normal",10,"normal",handler_cant,False,"register","left",10,10))
#-------------------------------------------------------------------------------


#------------------------------------BOTONES------------------------------------
botones = Frame(root)

registro = Button(style_button(botones,"REGISTRARSE",5,5,"Releway",10,"normal",10,"normal",btn_registrarse,False,"register","left",10,10))

ingresar = Button(style_button(botones,"INGRESAR",5,5,"Releway",10,"normal",10,"normal",btn_ingresar,False,"signin","left",10,10))
#-------------------------------------------------------------------------------
root.mainloop()

