import turtle

#Initializes turtles
def iTurtle(Shape, Color):
    nTurtle = turtle.Turtle()
    nTurtle.shape(Shape)
    nTurtle.color(Color)
    return nTurtle

#Set backdrop
def backdrop():
    window = turtle.Screen()
    window.bgcolor("green")
    return window

#Create a cursor that draws a square 
def draw_square():
    jake = iTurtle("turtle", "yellow")
    for x in range(4):
        jake.forward(100)
        jake.right(90)

#Creates a circle of squares
def square_loop():
    jake = iTurtle("turtle", "yellow")
    for i in range(36):
        for x in range(4):
            jake.forward(100)
            jake.right(90)
        jake.right(10)
#Create a cursor that makes a circle
def draw_circle():
    raymond = iTurtle("arrow", "blue")
    raymond.circle(100)

#Create a cursor that makes a triangle
def draw_triangle():
    bob = iTurtle("classic", "red")
    bob.forward(90)
    bob.left(135)
    bob.forward(120)
    bob.left(135)
    bob.forward(90)

class fractal:
    def __init__(self, level, Shape, Color):
        self.level = level
        self.length = 2
        self.turtwig = turtle.Turtle()
        self.turtwig.shape(Shape)
        self.turtwig.color(Color)
        self.turtwig.penup()
        self.turtwig.setpos(-100,-100)
        self.turtwig.pendown()

    def draw_fractal(self, level):
        if(level != 0):
            self.draw_triangle(level)
            level -= 1
            self.draw_fractal(level)
            self.turtwig.penup()
            self.turtwig.forward(30*(self.length**level))
            self.turtwig.pendown()
            self.draw_fractal(level)
            self.turtwig.penup()
            self.turtwig.backward(30*(self.length**level))
            self.turtwig.pendown()
            self.turtwig.penup()
            self.turtwig.left(60)
            self.turtwig.forward(30*(self.length**level))
            self.turtwig.right(60)
            self.turtwig.pendown()
            self.draw_fractal(level)
            self.turtwig.penup()
            self.turtwig.left(60)
            self.turtwig.backward(30*(self.length**level))
            self.turtwig.right(60)
            self.turtwig.pendown()
        else:
            self.draw_triangle(level)

    def draw_triangle(self, level):
        if(level == 0):
            self.turtwig.begin_fill()
        for e in range(3):
            self.turtwig.forward(30*(self.length**level))
            self.turtwig.left(120)
        if(level == 0):
            self.turtwig.end_fill()
    
mainWin = backdrop()
Fractal = fractal(4, "turtle", "blue")
Fractal.draw_fractal(Fractal.level)
#draw_fractal(4)
#square_loop()
#draw_square()
#draw_circle()
#draw_triangle()
mainWin.exitonclick()

