import turtle
import time
# ---> Declare Vars
width = 500
height = 900
#? ---> Create turtle object for the Window
wn = turtle.Screen()
wn.setup(width, height) # Window Size
#wn.screensize(canvwidth=(width-100), canvheight=height)
# wn.bgcolor("white") # Background Color
wn.bgpic('rocket-launch-2/rocket-basen.gif') #Background Base
wn.title("Lanzamiento del SpaceTIC Rocket") # Set title
wn.cv._rootwindow.resizable(False, False) # Lock window resize 

#? --> Create turtle object for the Rockect
rocket = turtle.Turtle() # Create Rocket object
# --> Add new route
#? --> Create turtle object for the Writer
houston = turtle.Turtle()
houston.hideturtle()
houston.penup()
houston.goto(-30,300)
houston.write("⌛", font=("Arial",30,'normal'))

# --> Put on base
rocket.penup()
rocket.setpos(-30, -245)

# --> Add Rocket graphic
wn.addshape('rocket-launch-2/new-rocket.gif')
rocket.shape('rocket-launch-2/new-rocket.gif')

# ---> Put on Launch Position
rocket.left(90)
# ---> Count
for x in range(10,-1,-1): 
    houston.clear()
    houston.write(x, font=("Arial",50,'normal'))
    time.sleep(1)

houston.clear()
# ---> Tur On Raptor Motor
wn.update()
time.sleep(1)
wn.addshape('rocket-launch-2/start-rocket.gif') #Change the Rocket Image
rocket.shape('rocket-launch-2/start-rocket.gif')

# ---> Go to Fly

wn.delay(20)
rocket.speed(1) #Adjust Velocity
rocket.forward(height)
wn.mainloop()