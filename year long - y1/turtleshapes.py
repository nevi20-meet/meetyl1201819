import turtle
''''
turtle.pencolor("light blue")
turtle.goto(200,0)
turtle.pencolor("pink")
turtle.goto(50,-150)
turtle.pencolor("purple")
turtle.goto(100,100)
turtle.pencolor("light green")
turtle.goto(150,-150)
turtle.pencolor("blue")
turtle.goto(0,0)
'''
'''
turtle.fillcolor("light blue")
turtle.begin_fill()
turtle.goto(200,0)
turtle.goto(200,-150)
turtle.goto(100,-300)
turtle.goto(0,-150)
turtle.goto(0,0)
turtle.end_fill()
'''
turtle.speed(0)
for circle_1 in range(1000):
	turtle.forward(300)
	turtle.right(50)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	turtle.goto(0,0)
	turtle.right(2)
	turtle.pendown()
