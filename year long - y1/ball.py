from turtle import *

class Ball (Turtle):
	def __init__ (self, x, y, dx,dy, radius, color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.radius= radius
		self.shape("circle")
		self.shapesize(radius/10)
		self.color(color)
		
	def move (self, screen_width, screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.radius
		left_side_ball = new_x - self.radius
		top_side_ball = new_y + self.radius
		bottom_side_ball = new_y - self.radius
		self.goto(new_x, new_y)
		if right_side_ball >= screen_width:
			self.dx = -self.dx
		if left_side_ball <= -screen_width:
			self.dx = -self.dx
		if top_side_ball >= screen_height:
			self.dy = -self.dy
		if bottom_side_ball <= -screen_height:
			self.dy = -self.dy 
