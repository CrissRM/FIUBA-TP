import tkinter as tk
from utils.estilos_formatos import estilos


def Label(estilo):
  Label = tk.Label(
    estilo["root"],
    text=estilo["text"],
    background=estilos["BACKGROUND_PRIMARY"],
    foreground=estilos["FOREGROUND_PRIMARY"],
    padx=10,
    pady=10,
    font=(estilo["font_family"],estilo["font_size"],estilo["font_slant"]),
    width=estilo["width"],
    anchor=estilo["anchor"]
  )
  Label.pack(side=estilo["side"],padx=estilo["margin_x"],pady=estilo["margin_y"])

