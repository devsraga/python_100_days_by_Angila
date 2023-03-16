from turtle import Turtle, Screen


def main():
    timy_the_turtle = Turtle()
    timy_the_turtle.shape("turtle")
    timy_the_turtle.color("red")
    draw_squire_cw(timy_the_turtle)
    draw_squire_ccw(timy_the_turtle)
    screen = Screen()
    screen.exitonclick()


def draw_squire_cw(turtle):
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)


def draw_squire_ccw(turtle):
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)


if __name__ == "__main__":
    main()
