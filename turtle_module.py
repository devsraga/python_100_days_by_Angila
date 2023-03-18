import random
import turtle
from turtle import Turtle, Screen, colormode
import colorgram




def main():
    # defining the first turtle timy
    timy_the_turtle = Turtle()

    # turtle parameters
    timy_the_turtle.shape("turtle")
    timy_the_turtle.color("red")
    turtle.colormode(255)


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
    draw_multi_polygon(timy_the_turtle, size=100, polygon_num=10)
    timy_the_turtle.clear()

    # Random walk by a turtle
    random_walk(timy_the_turtle, pensize=10, times=200, speed="fastest")
    timy_the_turtle.clear()

    # Drawing spirograph
    draw_spirograph(turtle, radius=100, size_gap=10, speed="fastest", pensize=2)
    timy_the_turtle.clear()

    # Drawing Hirst painting
    draw_hirst_painting(timy_the_turtle, size=10)
    timy_the_turtle.clear()

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
    previous_pesize = turtle.pensize()
    turtle.pensize(10)
    for i in range(3, polygon_num):
        draw_polygon(turtle, i, size, colour=rand_color_all())
    turtle.pensize(previous_pesize)
    print(previous_pesize)

# random colours
def rand_color():
    colour_list = ["red", "green", "blue", "black", "orange red", "yellow", "pink", "orange red"]
    random_color = random.choice(colour_list)
    return random_color


# hist colors
def rand_hist_color():
    # Extract 6 colors from an image.
    hist_colors_extracted = colorgram.extract('Hist_color_pic.jpg', 10)
    hist_colors = []
    for color in hist_colors_extracted:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = (r, g, b)
        hist_colors.append(rgb)
    rand_hist_color = random.choice(hist_colors)
    hist_colors_filter = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
(134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
(232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
(19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
(176, 192, 208), (168, 99, 102)]
    rand_hist_color_filter = random.choice(hist_colors_filter)
    return rand_hist_color_filter


# multiple random colors
def rand_color_all():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


# Random walk by a turtle
def random_walk(turtle, pensize=10, times=100, speed="fastest"):
    setheading_list = [0, 90, 180, 270]
    turtle.pensize(pensize)
    for i in range(times):
        turtle.speed(speed)
        turtle.setheading(random.choice(setheading_list))
        color = rand_color_all()
        turtle.pencolor(color)
        turtle.fd(30)
    turtle.penup()
    turtle.home()
    turtle.pendown()


# Drawing spirograph
def draw_spirograph(turtle, radius=100, size_gap=10, speed="fastest", pensize=2):
    turtle.speed(speed)
    turtle.pensize(pensize)
    times = round(360/size_gap)
    for i in range(times):
        turtle.pencolor(rand_color_all())
        turtle.circle(radius)
        turtle.rt(size_gap)


# Drawing Hirst painting
def draw_hirst_painting(turtle, size=10):
    print(rand_hist_color())
    turtle.speed("fastest")
    turtle.penup()
    turtle.hideturtle()
    turtle.rt(135)
    turtle.fd(300)
    turtle.setheading(0)
    for j in range(size):
        for i in range(size):
            turtle.dot(size*3, rand_hist_color())
            turtle.fd(size*6)
        turtle.setheading(90)
        turtle.fd(size*6)
        turtle.setheading(180)
        turtle.fd(size*size*6)
        turtle.setheading(0)


if __name__ == "__main__":
    main()
