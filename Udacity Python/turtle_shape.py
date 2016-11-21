import turtle

def square(size, caller):
	for i in range(1,size):
		caller.forward(100)
		caller.right(90)

def drawSquare():

	window = turtle.Screen()
	window.bgcolor('blue')
	bane = turtle.Turtle()
	bane.color('black')
	bane.shape('turtle')
	bane.speed(20)
	for i in range(1,40):
		square(5,bane)
		bane.right(10)
	window.exitonclick()

drawSquare()
