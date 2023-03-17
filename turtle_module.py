import random
from turtle import Turtle, Screen


def main():
    # defining the first turtle timy
    timy_the_turtle = Turtle()

    # turtle parameters
    timy_the_turtle.shape("turtle")
    timy_the_turtle.color("red")
    timy_the_turtle.colormode(255)

    # drawing cw_squire by timy
    draw_squire_cw(timy_the_turtle)
    timy_the_turtle.clear()

    # drawing ccw_squire by timy
    draw_squire_ccw(timy_the_turtle)
    timy_the_turtle.clear()

    # Drawing a dashed line of any length
    draw_dash_line(timy_the_turtle, length=200, dash_size=4, gap_size=4)
    timy_the_turtle.clear()

    # drawing a polygon by the turtle
    timy_the_turtle.penup()
    timy_the_turtle.home()
    draw_polygon(timy_the_turtle, sides=6, size=50, colour="green")
    timy_the_turtle.clear()

    # Drawing a multi polygon with different size
    timy_the_turtle.penup()
    timy_the_turtle.home()
    draw_multi_polygon(timy_the_turtle, size=50, polygon_num=10)
    # timy_the_turtle.clear()

    # Setting screen parameters
    screen = Screen()
    screen.exitonclick()


# drawing cw_squire by timy
def draw_squire_cw(turtle):
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)


# drawing ccw_squire by timy
def draw_squire_ccw(turtle):
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)


# Drawing a dashed line of any length
def draw_dash_line(turtle, length, dash_size=4, gap_size=4):
    iterations = round(length/(dash_size+gap_size))
    for i in range(iterations):
        turtle.fd(dash_size)
        turtle.penup()
        turtle.fd(gap_size)
        turtle.pendown()


# drawing a polygon by the turtle
def draw_polygon(turtle, sides, size, colour="red"):
    angle = (360/sides)
    colour_before = turtle.pencolor()
    turtle.color(colour)
    if not turtle.isdown():
        turtle.pendown()
    for i in range(sides):
        turtle.fd(size)
        turtle.lt(angle)
    turtle.color(colour_before)


# Drawing a multi polygon with different size
def draw_multi_polygon(turtle, size, polygon_num):
    for i in range(3, polygon_num):
        draw_polygon(turtle, i, size, colour=rand_color())


def rand_color():
    colour_list = ["red", "green", "blue", "black", "orange red", "yellow", "pink", "orange red"]
    random_color = random.choice(colour_list)
    return random_color

def rand_color_all():


if __name__ == "__main__":
    main()
