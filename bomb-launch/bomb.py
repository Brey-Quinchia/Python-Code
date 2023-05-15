import turtle 

# --> Window Object 
wn = turtle.Screen()
wn.setup(1200,600)
wn.cv._rootwindow.resizable(False, False)
wn.title("Lanzamiento de Proyectil")
# --> Turtle Object 
bomb = turtle.Turtle()

bomb.penup()
bomb.bk(500)
bomb.rt(90)
bomb.fd(200)
bomb.lt(90)
bomb.pd()
bomb.lt(45)
wn.addshape('assets/little-boy.gif')
bomb.shape('assets/little-boy.gif')
bomb.penup()
bomb.speed(3)
bomb.circle(-600,90)
wn.addshape('assets/fire2.gif')
bomb.shape('assets/fire2.gif')
wn.mainloop()