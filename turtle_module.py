from turtle import Turtle, Screen


def main():
    # defining the first turtle timy
    timy_the_turtle = Turtle()

    # turtle parameters
    timy_the_turtle.shape("turtle")
    timy_the_turtle.color("red")

    # drawing cw_squire by timy
    draw_squire_cw(timy_the_turtle)

    # drawing ccw_squire by timy
    draw_squire_ccw(timy_the_turtle)

    # Drawing a dashed line of any length
    draw_dash_line(timy_the_turtle, 200, 4, 4)

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
def draw_dash_line(turtle, length, dash_size, gap_size):
    iterations = round(length/(dash_size+gap_size))
    for i in range(iterations):
        turtle.fd(dash_size)
        turtle.penup()
        turtle.fd(gap_size)
        turtle.pendown()


if __name__ == "__main__":
    main()
