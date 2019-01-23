import turtle
import time
import random
from ball import Ball

turtle.tracer (0,0)
turtle.hideturtle()
global running 
running = True 
sleep = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball (0, 0, 7, 5, 10, "pink")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS=[]
for i in range(NUMBER_OF_BALLS):
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	color =(random.random(), random.random(), random.random())
	NEW_BALL = Ball(10,10,10,10,10,"red")
	BALLS.append(NEW_BALL)

def move_all_balls(BALLS):
	for ball in BALLS:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)	

def collide (ball_a, ball_b):
	if ball_a == ball_b:
		return False
	x1 = ball_a.xcor()
	y1 = ball_a.ycor()
	x2 = ball_b.xcor()
	y2 = ball_b.ycor()
	d = ((x1-x2)**2+(y1-y2)**2)**0.5
	if ball_a.radius + ball_b.radius >= d:
		return True
	else:
		return False
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide (ball_a, ball_b):
				radius1 = ball_a.radius
				radius2 = ball_b.radius

				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				color =(random.random(), random.random(), random.random())

				if radius1 >= radius2:
					ball_a.radius += 1
					ball_a.shapesize(radius/10)
					ball_b.shapesize(radius/10)
					ball_b.radius = radius
					ball_b.penup()
					ball_b.goto(x,y)
					ball_b.dx=dx
					ball_b.dy=dy
					ball_b.shape("circle")
					ball_b.color(color)	
				else:
					ball_b.radius += 1
					ball_b.shapesize(radius/10)
					ball_a.shapesize(radius/10)
					ball_a.radius = radius
					ball_a.penup()
					ball_a.goto(x,y)
					ball_a.dx=dx
					ball_a.dy=dy
					ball_a.shape("circle")
					ball_a.color(color)	

def check_myball_collision():
	for ball in BALLS:
		if collide (MY_BALL, ball):
			radius1 = MY_BALL.radius
			radius2 = ball.radius
			if radius1 <= radius2:
				return False
			else:
				MY_BALL.radius += 1
				MY_BALL.shapesize(radius/10)
				ball.shapesize(radius/10)
				ball.radius = radius
				ball.penup()
				ball.goto(x,y)
				ball.dx=dx
				ball.dy=dy
				ball.shape("circle")
				ball.color(color)	
	return True

def movearound (event):
	x = event.x - SCREEN_WIDTH
	y = SCREEN_HEIGHT - event.y
	MY_BALL.goto(x,y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while running:
	SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
	SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)
	move_all_balls(BALLS)
	check_all_balls_collision()
	running = check_myball_collision()
	turtle.update()
	time.sleep(sleep)