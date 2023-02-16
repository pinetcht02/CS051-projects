"""
    CS051P Lab Assignments: Recursive Graphics

    Name: Pine Netcharussaeng

    Date: 10/27/22

    The goal of this assignment is to familiarize you with recursion,
    including thinking and writing recursive functions.
"""
from turtle import *
from math import sqrt
speed(0)

def draw_triangle(length, color):
    """
    Draw equilateral triangle, from the current position.
    :param length: (int) side length in pixels
    :param color: (string) line color

    end up in original position and heading
    """
    # set color and drop the pen
    pencolor(color)
    pendown()

    # three sides, w/120 degree exterior angles
    # Note: this function demostrates poor style (it uses repeated code)
    forward(length)
    left(120)
    forward(length)
    left(120)
    forward(length)
    left(120)

    # we should now be at our original position/heading



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
        left(360 / n)


def stairs(x, y, length):
    """

    :param x: (int) the starting x coordinate
    :param y: (int) the starting y coordinate
    :param length: (int) the starting side length of a square
    :return: (int) the number of times a square is drawn
    """
    # if the side length of a square is less than 10, return 0
    if length <= 10:
        return 0
    else:
        # draw first big square
        penup()
        goto(x, y)
        pendown()
        draw_polygon(4, length)

        return stairs(x, y+length, length // 2) + stairs(x+length, y, length // 2) + 1

def move_forward():
    """
    places turtle in random coordinates in the display window

    :return: None
    """
    penup()
    forward(100)
    pendown()

def main_part1():
    # draw a dot of size 5 in the center of the screen
    dot(5)

    # fancy geometry to calculate the starting point of an equilateral triangle at
    # the center of the screen
    # If you understand the math, great! If not, that's fine. Don't spend time
    # worrying about it. This isn't a geometry class.
    side_len = 60
    triangle_height = sqrt(side_len**2 - (side_len/2)**2) # use Pythagorean thm
    centroid_height = triangle_height/3  # centroid is 1/3 up the height
    y_init = -1 * centroid_height
    x_init = -1 * (side_len/2)

    # draw a single triangle of size 60 in the center of the screen
    penup()
    setposition(x_init,y_init)
    pendown()
    setheading(0)
    draw_triangle(60, "black")

    # draw triangle
    move_forward()
    draw_polygon(3, 50)

    # draw square
    move_forward()
    draw_polygon(4, 50)

    # draw hexagon
    move_forward()
    draw_polygon(6, 30)

    # draw 16-sided polygon
    move_forward()
    draw_polygon(12, 20)

    # draw 32-sided polygon
    move_forward()
    draw_polygon(32, 10)

    # draw stairs
    stairs(-500,-270,512)

    # hide turtle and preserve the display
    hideturtle()


def snowflake(x, y, size):
    """

    :param x: (int) the starting x coordinate
    :param y: (int) the starting y coordinate
    :param size: (int) the starting length of the arm
    :return: (int) the number of arms drawn in the end of the function
    """
    # initialize counter
    counter = 0

    # go to the desired x, y coordinate
    penup()
    goto(x, y)
    pendown()

    # if arm size is less than 5, draw red dot at the end of arm
    if size < 5:
        dot(5, "red")
    else:
        # draw the eight arms of the snowflake
        for num in range(8):
            penup()
            goto(x, y)
            pendown()
            forward(size)
            right(45)
            # add 1 for each arm
            counter += 1
        # add counter of each snowflake's arm into the initial counter
        counter += snowflake(x + size, y, size / 3)
        counter += snowflake(x, y + size, size / 3)
        counter += snowflake(x - size, y, size / 3)
        counter += snowflake(x, y - size, size / 3)

    # return number of arms
    return counter



def main():
    print(snowflake(0, 0, 200))
    hideturtle()
    done()


if __name__ == '__main__':
    # main_part1()  # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1
