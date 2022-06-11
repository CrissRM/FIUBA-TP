import tkinter as tk
from utils.estilos_formatos import estilos
from formularios.formulario_registro import formulario_registro
from formularios.formulario_ingreso import formulario_ingreso
from componentes.Label import Label
from componentes.Button import Button
from componentes.Frame import Frame

def btn_registrarse():
  print("funciona ")
  form_registro = formulario_registro(root,registro,ingresar)
  form_registro.pack()
  
  registro["state"] = "disabled"
  ingresar["state"] = "disabled"
  
def btn_ingresar():
  form_ingreso = formulario_ingreso(root,registro,ingresar)
  form_ingreso.pack()
  registro["state"] = "disabled"
  ingresar["state"] = "disabled"


root = tk.Tk()
root.title("FIUBLE - SERPIENTE")
root.geometry("+300+200")
root.minsize(width=700,height=400)
root.configure(background=estilos["BACKGROUND_PRIMARY"])

style_label = {
    "root": root,
    "text": "FIUBELE - SERPIENTE",
    "padding_x": 5,
    "padding_y":5,
    "margin_x": 10,
    "margin_y": 10,
    "font_family": "Raleway",
    "font_size": 25,
    "font_slant": "roman",
    "side": "top",
    "width":25,
    "anchor": "center"
  }

Label(style_label)

botones = Frame(root)

estilos = {
    "root": botones,
    "text": "REGISTRARSE",
    "padding_x": 5,
    "padding_y":5,
    "margin_x": 10,
    "margin_y": 10,
    "button_style": "register",
    "font_family": "Raleway",
    "font_size": 10,
    "font_slant": "roman",
    "state": "normal",
    "side": "left",
    "command": btn_registrarse
  }

registro = Button(estilos)

estilos["text"] = "INGRESAR"
estilos["button_style"] = "signin"
estilos["command"]= btn_ingresar

ingresar = Button(estilos)

root.mainloop()

