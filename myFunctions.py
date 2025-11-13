import turtle
from random import randint
bob = turtle.Turtle()

def comet (c, dist, angle):
    color = (c)
    for times in range(10):
        bob.width(times +2)
        bob.forward(dist)
        bob.left(angle)
def home():
  bob.penup()
  bob.home()
  bob.pendown()

def rainbow():
  bob.width(20)
  bob.color("red")
  bob.circle(60)
  bob.color("orange")
  bob.circle(50)
  bob.color("yellow")
  bob.circle(40)
  bob.color("green")
  bob.circle(30)
  bob.color("blue")
  bob.circle(20)
  bob.color("purple")
  bob.circle(10)
  
def circle ( radius, border_color, fill_color):
    bob.pencolor(border_color)
    bob.fillcolor(fill_color)
    bob.begin_fill()
    bob.circle(radius)
    bob.end_fill()

def polygon(sides, dist, color):
  angle = 360/sides
  bob.fillcolor(color)
  bob.begin_fill()
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
  bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def plus(c,distance):
  bob.color(c)
  for times in range(4):
    bob.forward(distance)
    bob.left(90)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(90)

def sun(x,y):
  jump(x,y)
  bob.pensize(10)
  bob.color("yellow")
  for times in range(10):
    polygon(3,20)
    bob.forward(30)
    bob.right(36)
  jump(16 + x,-75 + y)
  bob.pensize(20)
  bob.circle(30)
