#Calculadora con Python  
from tkinter import *   
#Creamos nuestra ventana
ventanaCalculadora = Tk()
#? Le colocamos un titulo a nuestra calculadora 
ventanaCalculadora.title("CALCULADORA")
#* ---------- Espacio reservado para variables
i = 0 
mgx = 1; 
mgy = 5; 
#* - - - - - - - - - - - - - - - - - - - - - -
#*----- Espacio reservado para funciones 
def value(valor):
    global i 
    showOperation.insert(i, valor)
    i = i+1
def do_operation(): #Funcion para realizar
    operation = showOperation.get() 
    result = eval(operation)
    showOperation.delete(0,END)
    showOperation.insert(0,result)
    i = 0
def delete(): 
    showOperation.delete(0, END) #Borrar el contenido de la caja de texto 
    i = 0

#*--------------------------------------
#? Entrada de texto o barra de resultados
showOperation = Entry(ventanaCalculadora, font=('Calibri 20'))
#? Posicionamos la operacion dentro de la ventana
showOperation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#* Creacion de los botones
#--> Maqueta de botones 
# Button(ventanaCalculadora, text="", width=5, height=2, bg="" )
#? Boton de borrar
bt_borrar = Button(ventanaCalculadora, text="AC", width=5, height=2, bg="red", command= lambda: delete() )
bt_borrar.grid(row=1, column=0, padx=mgx, pady=mgy)
#? Boton de parentesis '('
bt_bracket1 = Button(ventanaCalculadora, text="(", width=5, height=2, bg="yellow", command= lambda: value('('))
bt_bracket1.grid(row=1, column=1, padx=mgx, pady=mgy)
#? Boton de parentesis ')'
bt_bracket2 = Button(ventanaCalculadora, text=")", width=5, height=2, bg="yellow", command= lambda: value(')') )
bt_bracket2.grid(row=1, column=2, padx=mgx, pady=mgy)
#? Boton de division '/'
bt_division = Button(ventanaCalculadora, text="/", width=5, height=2, bg="green", command= lambda: value('/') )
bt_division.grid(row=1, column=3, padx=mgx, pady=mgy)
#------------- Siguiente linea -------------------
#? Boton de N° 7 
bt_num7 = Button(ventanaCalculadora, text=7, width=5, height=2, bg="white", command= lambda: value(7) )
bt_num7.grid(row=2, column=0, padx=mgx, pady=mgy)
#? Boton de N° 8 
bt_num8 = Button(ventanaCalculadora, text=8, width=5, height=2, bg="white", command= lambda: value(8)  )
bt_num8.grid(row=2, column=1, padx=mgx, pady=mgy)
#? Boton de N° 9 
bt_num9 = Button(ventanaCalculadora, text=9, width=5, height=2, bg="white" , command= lambda: value(9) )
bt_num9.grid(row=2, column=2, padx=mgx, pady=mgy)
#? Boton de multiplicacion 'x'
bt_byX = Button(ventanaCalculadora, text='X', width=5, height=2, bg="green" , command= lambda: value('*') )
bt_byX.grid(row=2, column=3, padx=mgx, pady=mgy)
#------------- Siguiente Linea -------------------- 
#? Boton de N° 4 
bt_num4 = Button(ventanaCalculadora, text=4, width=5, height=2, bg="white" , command= lambda: value(4) )
bt_num4.grid(row=3, column=0, padx=mgx, pady=mgy)
#? Boton de N° 5 
bt_num5 = Button(ventanaCalculadora, text=5, width=5, height=2, bg="white", command= lambda: value(5)  )
bt_num5.grid(row=3, column=1, padx=mgx, pady=mgy)
#? Boton de N° 6 
bt_num6 = Button(ventanaCalculadora, text=6, width=5, height=2, bg="white" , command= lambda: value(6) )
bt_num6.grid(row=3, column=2, padx=mgx, pady=mgy)
#? Boton de multiplicacion 'x'
bt_plus = Button(ventanaCalculadora, text='+', width=5, height=2, bg="green" , command= lambda: value('+') )
bt_plus.grid(row=3, column=3, padx=mgx, pady=mgy)
#------------- Siguiente Linea -------------------- 
#? Boton de N° 1
bt_num1 = Button(ventanaCalculadora, text=1, width=5, height=2, bg="white" , command= lambda: value(1) )
bt_num1.grid(row=4, column=0, padx=mgx, pady=mgy)
#? Boton de N° 2 
bt_num2 = Button(ventanaCalculadora, text=2, width=5, height=2, bg="white" , command= lambda: value(2) )
bt_num2.grid(row=4, column=1, padx=mgx, pady=mgy)
#? Boton de N° 3 
bt_num3 = Button(ventanaCalculadora, text=3, width=5, height=2, bg="white" , command= lambda: value(3) )
bt_num3.grid(row=4, column=2, padx=mgx, pady=mgy)
#? Boton de resta '-'
bt_rest = Button(ventanaCalculadora, text='-', width=5, height=2, bg="green" , command= lambda: value('-') )
bt_rest.grid(row=4, column=3, padx=mgx, pady=mgy)
#------------- Siguiente Linea -------------------- 
#? Boton de N° 0
button0 = Button(ventanaCalculadora, text="0", width= 16, height=2, command= lambda: value(0) )
button0.grid(row=5, column=0,columnspan=2, padx=0, pady=0)

#? Boton del '.' 
bt_point = Button(ventanaCalculadora, text='.', width=5, height=2, bg="white" , command= lambda: value('.') )
bt_point.grid(row=5, column=2, padx=mgx, pady=mgy)
#? Boton del '=' 
bt_result = Button(ventanaCalculadora, text='=', width=5, height=2, bg="white" , command= lambda: do_operation() )
bt_result.grid(row=5, column=3, padx=mgx, pady=mgy)


#!lINEA IMPORTANTE
ventanaCalculadora.mainloop()


