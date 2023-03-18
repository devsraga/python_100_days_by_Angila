
from turtle import Turtle, Screen
import random


def main():
    screen = Screen()
    screen.listen()
    screen.onkey(go_straight, "Up")
    screen.onkey(go_back, "Down")
    screen.onkey(turn_right, "Right")
    screen.onkey(turn_left, "Left")
    screen.onkey(clear, "space")
    screen.exitonclick()


def go_straight():

    timy.fd(15)


def go_back():
    timy.back(15)


def turn_left():
    timy.lt(10)


def turn_right():
    timy.rt(30)


def clear():
    timy.clear()
    timy.penup()
    timy.home()
    timy.pendown()





if __name__ == "__main__":
    timy = Turtle()
    timy.shape("turtle")
    timy.color("black")
    main()
