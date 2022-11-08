#Calculadora con Python  
from tkinter import *   
#Creamos nuestra ventana
ventanaCalculadora = Tk()
#? Le colocamos un titulo a nuestra calculadora 
ventanaCalculadora.title("CALCULADORA")
#*----- Espacio reservado para funciones 

#*--------------------------------------
#? Entrada de texto o barra de resultados
showOperation = Entry(ventanaCalculadora, font=('Calibri 20'))
#? Posicionamos la operacion dentro de la ventana
showOperation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#* Creacion de los botones
bt_borrar = Button(ventanaCalculadora, text="AC", width=5, height=2, bg="red" )
bt_borrar.grid(row=1, column=0, padx=5, pady=5)
#!lINEA IMPORTANTE
ventanaCalculadora.mainloop()


