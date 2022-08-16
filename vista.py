import tkinter
from tkinter import *
from tkinter import messagebox as MessageBox
from methods import Automata

root = Tk()
root.title("comprobacion expresiones regulares ")
root.config(bg="#1B2631")
root.resizable(0, 0)

miFrame = Frame()
miFrame.pack(fill="both", expand=True)
miFrame.config(bg="#1B2631")
miFrame.config(width=500, height=700)

labelentero = Label(miFrame, text="digite la entrada :",font=("courier", 12), justify=tkinter.CENTER)
labelentero.grid(row=1, column=1, pady=10)
labelentero.config(fg="white",bg="#1B2631",font=("courier",12))

variableText= StringVar()
entryentero = Entry(miFrame, bg="#F7F9F9", font=("courier",30), textvariable=variableText)
entryentero.grid(row=2, column=1,ipadx=50, ipady=30, padx=20, pady=10)




def test(value):
    automatita = Automata()
    MessageBox.showinfo("RESULTADO",automatita.validacion(value)) # título, mensaje

def setText(value):
    variableText.set(value)

Button(root, text="Clícame", command=lambda : [test(entryentero.get()), setText("")]).pack()
root.mainloop()



