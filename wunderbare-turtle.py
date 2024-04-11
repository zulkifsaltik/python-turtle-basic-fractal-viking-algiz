# This is for the wunderbare "Gebes Kaplumbaga"
import turtle

t = turtle.Turtle(visible=False)
s = t.getscreen()

s.title("Hey, Wunderbare Turtle!")
s.bgcolor("black")
t.speed(0)

# Fractals ~ Draw Circles
def circle(angle,rangex,pencolor,pensize,pos_x, pos_y):
    t.pencolor(pencolor)
    t.pensize(pensize)
    t.penup()
    t.goto(pos_x, pos_y)
    t.pendown()
    for x in range(rangex):
        t.circle(x)
        t.left(angle)

# Algiz ~Draw Algiz 
def algiz(pencolor, pensize):
    t.pencolor(pencolor)
    t.pensize(pensize)
    t.penup()
    
    # Algiz Double
    t.home()
    t.pendown()
    t.goto(0,80)
    t.goto(0,40)
    t.goto(40,80)
    t.goto(0,40)
    t.goto(-50,80)
    t.penup()
    t.home()
    t.pendown()
    t.goto(0,-80)
    t.goto(0,-40)
    t.goto(40,-80)
    t.goto(0,-40)
    t.goto(-40,-80)
    
    # Algiz 
    '''
    t.goto(50,50)
    t.pendown()
    t.home()
    t.goto(-50,50)
    t.home()
    t.goto(0,45)
    t.home()
    t.goto(0,-60)
    '''
#Call Functions
circle(60,50,"#912BBC",1,150,150)
circle(60,50,"#D875C7",1,-150,150)
circle(60,50,"#E9A89B",1,-150,-150)
circle(60,50,"#FFEBB2",1,150,-150)

circle(60,50,"#FFBFBF",1,-300,0)
circle(60,50,"#7EAA92",1,300,0)
circle(60,50,"#9ED2BE",1,0,300)
circle(60,50,"#C8E4B2",1,0,-300)

circle(60,100,"#C70039",1,0,0)

# Call Algiz 
algiz("#FFFFFF",10)
s.exitonclick() 

