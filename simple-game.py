#Creacion de un minijueo de tic tac toe usando python 
from tkinter import  *
gm_wd = Tk()
gm_wd.title("Tic Tac Toe")
gm_wd.geometry("400x300")
#... 
#* Creacion de los botones 
buttonA1 = Button(gm_wd, width=15, height=5)
buttonA2 = Button(gm_wd, width=15, height=5)
buttonA3 = Button(gm_wd, width=15, height=5)
buttonB1 = Button(gm_wd, width=15, height=5)
buttonB2 = Button(gm_wd, width=15, height=5)
buttonB3 = Button(gm_wd, width=15, height=5)
buttonC1 = Button(gm_wd, width=15, height=5)
buttonC2 = Button(gm_wd, width=15, height=5)
buttonC3 = Button(gm_wd, width=15, height=5)
buttonA1.grid(row=0, column=0, padx=5, pady=5)
buttonA2.grid(row=0, column=1, padx=5, pady=5)
buttonA3.grid(row=0, column=2, padx=5, pady=5)
buttonB1.grid(row=1, column=0, padx=5, pady=5)
buttonB2.grid(row=1, column=1, padx=5, pady=5)
buttonB3.grid(row=1, column=2, padx=5, pady=5)
buttonC1.grid(row=2, column=0, padx=5, pady=5)
buttonC2.grid(row=2, column=1, padx=5, pady=5)
buttonC3.grid(row=2, column=2, padx=5, pady=5)
#!Importante siempre el mainloop 
gm_wd.mainloop()