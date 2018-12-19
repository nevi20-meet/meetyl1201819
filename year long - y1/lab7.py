from turtle import *
import turtle
import random
import math

class Ball(Turtle):
	def __init__(self, radius, color, speed,dx,dy,x,y):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.dx=dx
		self.dy=dy
		self.penup()
		self.goto(x,y)
	def move (self):
		self.goto(self.xcor()+self.dx,self.ycor()+self.dy)
	def borders(self):
		high = 300
		low = -300
		left = -300
		right = 300
		if self.xcor()>right or self.xcor()<left:
			self.dx=-self.dx
		if self.ycor()>high or self.ycor()<low:
			self.dy= -self.dy
			
turtle.penup()
turtle.pensize(5)
turtle.goto(300,300)
turtle.speed(0)
for i in range (4):
	turtle.pendown()
	turtle.right(90)
	turtle.forward(600)
# code to create two ball objects here
ball1 = Ball(30, "light blue", 100,2,7, 150, 100)
ball2 = Ball (20, "pink", 70,3,5, -100, -150)

def check_collision(ball,ball2):
	# logic to check if the balls collide.
	x1=ball1.xcor()
	y1=ball1.ycor()
	x2=ball2.xcor()
	y2=ball2.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D<=ball.radius+ball2.radius:
		if ball1.radius>ball2.radius:
			ball2.goto(random.randint(-200,200),random.randint(-200,200))
			ball2.color(random.random(), random.random(), random.random())
			ball2.radius = random.randint(2,10)*10
			ball2.shapesize(ball2.radius/10)
		else:
			ball1.goto(random.randint(-200,200),random.randint(-200,200))
			ball1.color(random.random(), random.random(), random.random())
			ball1.radius = random.randint(2,10)*10
			ball1.shapesize(ball2.radius/10)
		random.randint(1,100)
		print ("colliding!!!")
while True:
	ball1.move()
	ball2.move()
	ball1.borders()
	ball2.borders()
	check_collision(ball1,ball2)



mainloop()	