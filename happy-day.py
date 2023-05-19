import turtle


wn = turtle.Screen()
wn.setup(900,900)

letras = turtle.Turtle()
turtle.bgcolor('black')
turtle.speed(0)
turtle.hideturtle() # --z Para Esconder la Tortuga 

#? --> Los colores de la Flor
colors = ["yellow","red","green","orange"]

turtle.goto(0,150) #* --> Para posicionar la flor un poco más arriba
for i in range(120): 
    for c in colors: 
        turtle.color(c) # --> Color del Petalo
        turtle.circle(200-i, 100) #--> Forma del Petalo
        turtle.lt(90)
        turtle.circle(200-i, 100) #--> Forma del Petalo
        turtle.rt(60)
        turtle.end_fill()

letras.penup() # --> Para evitar que turtle dibuje una linea
letras.color('pink') # Color de las letras
letras.goto(-250,-250) # Para posicionar la frase abajo de la flor
frase = "Feliz Mes Mamá" # Frase a dibujar
fontsize = 50# --> Tamaño de la fuente
letras.write(frase, font=("Courier",fontsize,'bold'))

turtle.mainloop()