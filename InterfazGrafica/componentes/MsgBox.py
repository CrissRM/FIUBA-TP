from tkinter import messagebox as mb

def msg_warning(msg):
  mb.showwarning("Advertencia",msg)

def msg_error(msg):
  mb.showerror("Error",msg)