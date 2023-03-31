import turtle
from turtle import Turtle, Screen, colormode
import random, time


def main():
    screen = Screen()
    # screen.screensize(800, 550)
    choice_to_play = True
    while choice_to_play:
        umpaier = Turtle()
        umpaier_settings(umpaier)
        choice = screen.textinput("Choice to play", "Do you want to play 'y', or 'n': ")
        choice = choice.lower()
        if choice == "y":
            turtles = []
            y_cor = [-140, -70, 0, 70, 140]
            colour_list = ["red", "green", "blue", "black", "orange red"]
            turtles = turtles_for_race(turtles, colour_list, y_cor)
            # user screen input
            input_color = user_input(screen, umpaier)
            winner = race(turtles)
            judgment(input_color, winner, umpaier)
            time.sleep(5)
            screen.clear()
        else:
            choice_to_play = False
            bye_msg(umpaier)
            umpaier.bye()

    screen.exitonclick()


# umpaier settings
def umpaier_settings(umpaier):
    umpaier.shape("turtle")
    umpaier.penup()
    umpaier.pensize(10)
    colormode(255)
    umpaier.color((128, 0, 0))
    umpaier.goto(0, 230)
    umpaier.rt(90)
    time.sleep(1)
    umpaier.home()
    umpaier.write("I am your 'UMPAIER' for 'TURTLE RACE'", True, align="center", font=('Arial', 15, 'normal'))
    umpaier.goto(0, 230)
    umpaier.rt(90)
    time.sleep(2)
    umpaier.clear()


# bye msg
def bye_msg(umpaier):
    umpaier.home()
    umpaier.write("Bye Bye", True, align="center", font=('Arial', 30, 'normal'))
    umpaier.goto(0, 230)
    umpaier.rt(90)
    time.sleep(1)
    umpaier.clear()
    umpaier.bye()


def turtles_for_race(turtles, colour_list, y_cor):
    for i in range(5):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.penup()
        turtle.color(colour_list[i])
        turtle.goto(-240, y_cor[i])
        turtles.append(turtle)
    return turtles


def turtles_on_pos(turtles, y_cor):
    for i in range(5):
        turtles[i].penup()
        turtles[i].goto(-240, y_cor[i])


# race
def race(turtles):
    is_racing = True
    while is_racing:
        for i in range(5):
            turtle = turtles[i]
            if turtle.xcor() < 240:
                turtle.fd(random.randint(2, 10))
            else:
                winner = turtle.pencolor()
                is_racing = False
    return winner


# Judgements
def judgment(input_color, winner,umpaier):
    desision = winner
    if desision == input_color:
        print(f"The bet you set for {input_color.upper()} color is Won!")
        umpaier.home()
        umpaier.write(f"The bet you set for {input_color.upper()} color is Won!", True, align="center", font=('Arial', 15, 'normal'))
        umpaier.goto(0, 230)
        umpaier.rt(90)
    else:
        print(f"Sorry you {input_color} lost the winner is {desision.upper()} color!")
        umpaier.home()
        umpaier.write(f"Sorry you {input_color} lost the winner is {desision.upper()} color!", True, align="center", font=('Arial', 15, 'normal'))
        umpaier.goto(0, 230)
        umpaier.rt(90)


# user screen input
def user_input(screen, umpaier):
    check_err = True
    while check_err:
        input_color = screen.textinput("bet to win", "Right the color which you want to win? - ")
        input_color = input_color.lower()
        if input_color == "red" or input_color == "green" or input_color == "blue" or input_color == "black"\
                or input_color == "orange red":
            check_err = False
            umpaier.clear()
        else:
            print("Enter Valid colour")
            umpaier.home()
            umpaier.write("Enter Valid colour", True, align="center", font=('Arial', 25, 'normal'))
            umpaier.goto(0, 230)
            umpaier.rt(90)
            check_err = True
    return input_color


if __name__ == "__main__":
    main()


