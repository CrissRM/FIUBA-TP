import tkinter as tk

root = tk.Tk()

nombre = tk.Label(
  root,
  text="Hola gente",
  padx=10,
  pady=20
)

nombre.pack(side="center")

root.mainloop()