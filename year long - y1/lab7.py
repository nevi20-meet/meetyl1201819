from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

# code to create two ball objects here
ball1 = Ball(10, "light blue", 50)
ball2 = Ball (20, "pink", 70)

def check_collision(ball,ball2):
	# logic to check if the balls collide.
	x1=ball1.xcor()
	y1=ball1.ycor()
	x2=ball2.xcor()
	y2=ball2.yocr()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D<=ball.radius+ball2.radius:
		print ("hi")
check_collision(ball1,ball2)
mainloop()	