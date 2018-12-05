import turtle
import random
turtle.colormode(255)
from turtle import Turtle
'''class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		turtle.shape("square")
		self.shapesize=10
	def random_color(self):
		# self.color("yellow")
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color((r,g,b))
		self.shape("square")


Square1 = Square(9)
Square1.random_color()
'''
class Hexagon(Turtle):
	def __init__ (self, size, color):
		Turtle.__init__(self)
		self.size = size
		turtle.begin_poly()
		turtle.penup()
		turtle.goto(50,-100)
		turtle.goto(100,-100)
		turtle.goto(150,0)
		turtle.goto(100,100)
		turtle.goto(50,100)
		turtle.goto(0,0)
		turtle.end_poly()
		h=turtle.get_poly()
		turtle.register_shape("Hexagon", h)
		self.shape("Hexagon")
		self.color(color)



hex = Hexagon(20,"yellow")

turtle.mainloop()
