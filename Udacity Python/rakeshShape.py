import turtle


def line1(caller):
    caller.right(-90)
    caller.forward(100)

def line8(caller):
	caller.right(-90)
	caller.forward(50)


def line2(caller):
    caller.right(90)
    caller.forward(50)


def line5(caller):
    caller.right(-135)
    caller.forward(70.71)


def line6(caller):
    caller.right(-45)
    caller.forward(50)


def line7(caller):
    caller.right(180)
    caller.forward(50)

# A closed C notation template which can be formed using 3 line2
def PNotation(caller):
	line1(caller)
	line2(caller)
	line2(caller)
	line2(caller)

def drawShape():
    window = turtle.Screen()
    window.bgcolor("blue")
    bane = turtle.Turtle()
    bane.speed(10)
    bane.shape("arrow")
    PNotation(bane)
    line5(bane)
    line6(bane)
    PNotation(bane)
    line7(bane)
    line2(bane)
    line8(bane)
    line1(bane)
    line7(bane)
    line5(bane)
    window.exitonclick()

drawShape()
