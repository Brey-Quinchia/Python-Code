import turtle #Importamos la libreria
import time 

logo = turtle.Turtle() # Creamos el objeto para el logo

wn = turtle.Screen() #Creamos el objeto para la ventana
# ---> definimos el valor de la Altura y ancho
width = 900
height = 900
wn.setup(width, height) #Asignamos el tamaño de la ventana
wn.bgcolor('white') #Color de fondo
wn.title('En la Tecno somos TIC')
# ---> Empezando a dibujar en el lienzo
def triangle(anglea, angleb): 
    smallLine = 30
    mediumLine = 50
    bigLine = 150
    logo.begin_fill()
    logo.color('white')
    logo.fillcolor("#39a900")
    logo.fd(bigLine)
    logo.left(anglea)
    logo.fd(bigLine)
    logo.left(angleb)
    logo.fd(smallLine)
    logo.left(angleb)
    logo.fd((bigLine-mediumLine))
    logo.right(anglea)
    logo.fd((bigLine-mediumLine))
    logo.left(angleb)
    logo.fd(smallLine)
    logo.end_fill()

def letras():
    letras = turtle.Turtle()
    letras.penup()
    letras.goto(-315,-10)
    letras.color("#39a900")
    letras.write("SENA", font=("Arial",80,'bold'))
    
#* ---> Llama al bloque de codigo del triangulo
logo.left(180)
logo.speed(9)
time.sleep(1)
triangle(120, 90)
logo.pu()
logo.goto((-175-150), 0)
logo.right(90)
time.sleep(2)
triangle(-120, -90)
logo.goto(-237.5, -140)
logo.right(30)
triangle(-120, -90)
logo.goto(-320,0)
logo.right(60)
letras()
# --> Dibujando el circulo
logo.goto(-130, 130)
logo.begin_fill()
logo.fillcolor("#39a900")
logo.circle(35)
logo.end_fill()
#? --> Debes Posicionar la tortuga para escribir el Nombre
#letras()
# ---> Ahora debes hacer el circulo 
#TODO: Intenta rellenar el circulo con begin_fill()
"""
logo.fillcolor("#39a900")
logo.begin_fill()
logo.circle(20)
logo.end_fill()
"""

# ---> Codigo para finalizar
turtle.done() #Para que la ventana permanezca abierta

