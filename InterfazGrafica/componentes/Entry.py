import tkinter as tk
from tkinter import font
from utils.estilos_formatos import estilos

def Entry(padre,is_password = False):
  if is_password:
    Entry = tk.Entry(
      padre,
      justify="left",
      font=(estilos["FONT_FAMILY"],estilos["FONT_SIZE_TEXT"]),
      show="*",
    )
  else:
    Entry =tk.Entry(
      padre,
      justify="left",
      font=(estilos["FONT_FAMILY"],estilos["FONT_SIZE_TEXT"])
    )
    
  Entry.pack(side="left")
  
  return Entry

    