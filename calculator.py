
from tkinter import *
from xml.dom import ValidationErr 
#? Creacion de la ventana 
window = Tk()
window.title("Calculator") # Titulo de la ventana 
#Definicion de funciones 
i = 0 

#? Entrada de texto 
inputText = Entry(window, font=("Calibri 20"))
inputText.grid(row=0, column=0, columnspan=4, padx=5, pady=5) #? Show the text in the window

def value(valor):
    global i 
    inputText.insert(i, valor)
    i = i+1
def delete(): 
    inputText.delete(0, END) #Borrar el contenido de la caja de texto 
    i = 0
def do_operation(): #Funcion para realizar
    operation = inputText.get() 
    result = eval(operation)
    inputText.delete(0,END)
    inputText.insert(0,result)
    i = 0
#* Creacion de Botones 
button1 = Button(window, text="1", width= 5, height=2, command= lambda: value(1))
button2 = Button(window, text="2", width= 5, height=2, command= lambda: value(2))
button3 = Button(window, text="3", width= 5, height=2, command= lambda: value(3))
button4 = Button(window, text="4", width= 5, height=2, command= lambda: value(4))
button5 = Button(window, text="5", width= 5, height=2, command= lambda: value(5))
button6 = Button(window, text="6", width= 5, height=2, command= lambda: value(6))
button7 = Button(window, text="7", width= 5, height=2, command= lambda: value(7))
button8 = Button(window, text="8", width= 5, height=2, command= lambda: value(8))
button9 = Button(window, text="9", width= 5, height=2, command= lambda: value(9))
button0 = Button(window, text="0", width= 16, height=2, command= lambda: value(0))
#... Other controllers 
button_delete = Button(window, text="AC", width= 5, height=2, command= lambda: delete())
button_brochA = Button(window, text="(", width= 5, height=2, command= lambda: value("("))
button_brochB = Button(window, text=")", width= 5, height=2, command= lambda: value(")"))
# Operations 
button_sum = Button(window, text="+", width= 5, height=2, command= lambda: value("+"))
button_rest = Button(window, text="-", width= 5, height=2, command= lambda: value("+"))
button_div = Button(window, text="/", width= 5, height=2, command= lambda: value("/"))
button_mult = Button(window, text="*", width= 5, height=2, command= lambda: value("*"))
button_result = Button(window, text="=", width= 5, height=2, command= lambda: do_operation())
button_point = Button(window, text=".", width=5, height=2, command= lambda: value("."))

#Agregar los botones en pantalla 
#* Again... 
# ? Alinear los botones con grid 
#... --> button_.grid(row=, column=, padx=5, pady=5)  
#Segunda fila
button_delete.grid(row=1, column=0, padx=5, pady=5)
button_brochA.grid(row=1, column=1, padx=5, pady=5) 
button_brochB.grid(row=1, column=2, padx=5, pady=5)
button_div.grid(row=1, column=3, padx=5, pady=5) 
#Tercera fila 
button7.grid(row=2, column=0, padx=5, pady=5)
button8.grid(row=2, column=1, padx=5, pady=5) 
button9.grid(row=2, column=2, padx=5, pady=5) 
button_mult.grid(row=2, column=3, padx=5, pady=5) 
#Fila 4 
button4.grid(row=3, column=0, padx=5, pady=5) 
button5.grid(row=3, column=1, padx=5, pady=5) 
button6.grid(row=3, column=2, padx=5, pady=5) 
button_sum.grid(row=3, column=3, padx=5, pady=5) 
#fila 5 
button1.grid(row=4, column=0, padx=5, pady=5) 
button2.grid(row=4, column=1, padx=5, pady=5) 
button3.grid(row=4, column=2, padx=5, pady=5) 
button_rest.grid(row=4, column=3, padx=5, pady=5) 
#Fila 6 
button0.grid(row=5, column=0,columnspan=2, padx=0, pady=0)
button_point.grid(row=5, column=2, padx=5, pady=5)
button_result.grid(row=5, column=3, padx=5, pady=5)
#!Importante siempre el mainloop 
window.mainloop()