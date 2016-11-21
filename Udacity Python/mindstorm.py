import turtle

def square(size, caller):
    for i in range(1, size):
        caller.forward(200)
        caller.right(90)


def random(size, caller):
    for i in range(1, size):
        caller.forward(100)
        caller.left(45)


def random_1(size, caller):
    for i in range(1, size):
        caller.left(45)
        caller.forward(100)


def random_2(size, caller):
    for i in range(1, size):
        caller.circle(100)
        caller.forward(20)


def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    Random = turtle.Turtle()
    Random.speed(20)
    random_2(30, Random)

    Bane = turtle.Turtle()
    Bane.color('black')
    square(40, Bane)
    Bane.speed(20)

    Batman = turtle.Turtle()
    Batman.color("black")
    random(40, Batman)
    Batman.speed(20)

    Joker = turtle.Turtle()
    random_1(40, Joker)
    Joker.speed(20)

    window.exitonclick()

draw_square()
