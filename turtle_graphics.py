"""
    CS051P Lab Assignments: Turtle Graphics

    Name: Pine Netcharussaeng

    Date:  10/20/22

    The goal of this assignment is to give you practice working with turtle graphics
"""

from turtle import *
import random

def draw_spirograph(n1,n2, pc, fc):
    pencolor(pc)
    fillcolor(fc)
    begin_fill()
    while True:
        forward(n1)
        left(n2)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

def draw_triangle(length, color):
    """
    draws a triangle

    :param length: length of side
    :param color: color of the side
    :return: a triangle
    """
    pencolor(color)
    for num in range(3):
        forward(length)
        left(120)

def draw_hexagon_triangle(length, color):
    """
    draws a hexagon

    :param length: length of the hexagon
    :param color: color of the hexagon
    :return: a hexagon
    """
    pencolor(color)
    for num in range(6):
        draw_triangle(length, color)
        left(60)




def main_part1():
    # draw first hexagon and move turtle
    draw_hexagon_triangle(100, "purple")
    penup()
    goto(-200, 0)
    pendown()

    # draw second hexagon and move turtle
    draw_hexagon_triangle(100, "pink")
    penup()
    goto(-400, 0)
    pendown()

    # draw third hexagon and move turtle
    draw_hexagon_triangle(100, "green")
    hideturtle()



def draw_polygon(n, length):
    """
    draws an n sided polygon

    :param n: (int) number of desired sides for polygon
    :param length: (int) the desired length of each side
    :return: None
    """
    # draw n sides
    for side in range(n):
        forward(length)

        # turn 360/n degrees
        right(360 // n)



def draw_spiral(increment, deg, n):
    """
    draws a spiral

    :param increment: (int) an increment for each time a side is drawn
    :param deg: (int) the degree that the spiral will turn
    :param n: (int) the number of sides
    :return: None
    """
    multiplier = 0
    # draw n sides
    for sides in range(n):

        # add 1 for increment multiplier
        multiplier += 1

        # increase increment by 1 each time a side is drawn
        if multiplier <= n:
            new_increment = increment * multiplier
        forward(new_increment)
        right(deg)



def rotate_repeat(k, n, length, drawing):
    """

    :param k: (int) the number of times to repeat the drawing
    :param n: (int) the number of sides of the drawing
    :param length: (int) the length of the side(s)
    :param drawing: (func) a function of desired drawing
    :return: None
    """
    for times in range(k):
        if drawing == draw_polygon:
            draw_polygon(n, length)
            left(360/k)
        elif drawing == draw_spiral:
            increment = length
            deg = random.randint(0, 180)
            draw_spiral(increment, deg, n)

def random_place():
    """
    places turtle in random coordinates in the display window

    :return: None
    """
    x = random.randint(-320, 320)
    y = random.randint(-270, 270)
    penup()
    goto(x, y)
    pendown()

def random_circle():
    """
    Generates random circles of different colors in the display window

    :return: None
    """
    # generate random coordinates for circle
    x = random.randint(-320, 320)
    y = random.randint(-270, 270)
    penup()
    goto(x, y)

    # assign different color for each quadrant
    # quadrant 1
    if x > 0 and y > 0:
        pencolor("darkorchid")
        fillcolor("mediumpurple")

    # quadrant 2
    elif x > 0 and y < 0:
        pencolor("teal")
        fillcolor("mediumseagreen")

    # quadrant 3
    elif x < 0 and y > 0:
        pencolor("goldenrod")
        fillcolor("gold")

    # quadrant 4
    else:
        pencolor("indianred")
        fillcolor("lightcoral")

    # begin drawing
    pendown()
    begin_fill()
    circle(10)
    end_fill()


def main():

    # draw two polygons
    for num in range(2):
        # randomize numbers
        n = random.randint(3, 10)
        length = random.randint(5, 50)

        # draw
        random_place()
        draw_polygon(n, length)

    # draw two more intricate polygons
    for num in range(1):
        # randomize numbers
        n = random.randint(3, 10)
        length = random.randint(5, 50)
        k = random.randint(2, 10)

        # draw one repeated polygon and repeated spiral
        random_place()
        rotate_repeat(k, n, length, draw_polygon)
        random_place()
        rotate_repeat(k, n, length, draw_spiral)

    # draw spirals
    for num in range(3):
        random_place()
        increment = random.randint(5, 15)
        deg = random.randint(20, 150)
        side = random.randint(10, 30)
        draw_spiral(increment, deg, side)

    # draw circles
    for num in range(20):
        random_circle()

    done()



if __name__ == '__main__':
    # main_part1()  # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1
