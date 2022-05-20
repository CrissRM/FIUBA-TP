from email.policy import strict
from sqlite3 import Row
from tkinter import *
from turtle import color

root = Tk()
root.resizable(0,0)

frm = Frame(root)
frm.pack()


frm_title = Frame(frm,width=700,height=50)
frm_title.config(bg="#121212")
frm_title.grid(row=0,column=0)


# title = Label(frm_title,text="FIUBLE")
# title.config(fg="#ffffff",bg="#121212",font=("Sans Serif",18))
# title.grid(row=0,column=0)
# title.grid_propagate(False)

# # title.place(x=345,y=20)

""" <--------------------------------- INPUTS --------------------------------->"""
# container_inputs = Frame(frm,width="600",height="400")
# container_inputs.config(bg="#121212")
# container_inputs.grid(row=1,columnspan=5)
# letter_1 = Entry(container_inputs,width=5).grid(row=1,column=0)
# letter_2 = Entry(container_inputs,width=5).grid(row=1,column=1)
# letter_3 = Entry(container_inputs,width=5).grid(row=1,column=2)
# letter_4 = Entry(container_inputs,width=5).grid(row=1,column=3)
# letter_5 = Entry(container_inputs,width=5).grid(row=1,column=4)

root.mainloop()