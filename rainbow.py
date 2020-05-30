import turtle
import time

def draw():
	colors = ['red', 'green', 'blue', 'orange', 'yellow', 'white', 'purple', 'brown', 'pink']
	turtle.pensize(10)
	turtle.bgcolor('black')
	turtle.speed(10000000)

	for x in range (10000000):
		turtle.pencolor(colors[x % len(colors)])
		turtle.pensize(x/30)
		turtle.forward(x)
		turtle.left(40)

draw()
time.sleep(5)