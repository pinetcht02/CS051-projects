"""
    CS051P Lab Assignments: PPM Image Modifier

    Name: Pine Netcharussaeng

    Date:   10/21/22

    The goal of this assignment is to give you practice working with lists
    by writing a program that manipulates image files in various ways.
"""
from math import sqrt


def decode(in_filename, out_filename):
    """

    :param in_filename: the file of the picture to be read
    :param out_filename: the new file to be altered
    :return: None
    """

    f_in = open(in_filename, "r")
    f_out = open(out_filename, "w")

    # counter for the lines
    counter = 0
    for line in f_in:
        counter += 1
        # start converting numbers after 3 header lines
        if counter <= 3:
            f_out.write(line)
        # split each line of the file
        else:
            each_line = line.split()

            # go through each number and decode the number
            for elem in each_line:
                if int(elem) % 3 == 0:
                    f_out.write("0 ")
                elif int(elem) % 3 == 1:
                    f_out.write("153 ")
                else:
                    f_out.write("255 ")
            f_out.write("\n")

    f_in.close()
    f_out.close()

def main_part1():
    decode("files/part1.ppm", "new_file.ppm")


def negate(line):
    """
    Takes a sequence of integers and returns negated integers

    :param line: (str) an input string containing rgb values
    :return: (str) an output string containing the negated rgb values
    """
    new_line = ""
    for elem in line.split():
        new_elem = 255 - int(elem)
        new_line = new_line + str(new_elem) + " "

    return new_line

def grey_scale(line):

    """
    takes a series of integers and converts every rgb value into a gray scale

    :param line: (str) a string containing a series of integers in multiple of three
    :return: (str) a string of output integers converted to their grey scale values
    """
    # create new list with grey value
    grey_line = ""

    # split elements in line
    value_list = line.split()

    # set up a counter for rgb values
    color_count = 0

    # set rgb according to index 1, 2, 3
    for elem in value_list:
        color_count = color_count + 1
        if color_count == 1:
            r = int(elem)
        if color_count == 2:
            g = int(elem)
        if color_count == 3:
            b = int(elem)

            # calculate the greyscale value and add to string
            grey = int(sqrt(r ** 2 + g ** 2 + b ** 2))

            # set greyscale value into 255 if it is more than 255
            if grey > 255:
                grey = 255

            # add value to grey_line
            grey_line = grey_line + (str(grey) + " ") * 3

            # reset color count
            color_count = 0

    return grey_line


def scale(image, row_scale, col_scale):
    """
    takes a series of integers (pixels) and reduce the width and height of an image

    :param image: a list of lists of a series of integers in multiples of three
    :param row_scale: (int) a number of desired multiple of row
    :param col_scale: (int) a number of desired multiple of column
    :return:  a list of lists of scaled row and column
    """
    # create final list of desired rows and columns
    final_list = []

    # take every row_scaleth list and put into new list
    for index in range(len(image)):
        sublist = []
        # find the row scaleth item
        if index % row_scale == 0:
            # find the col_scaleth item
            for j in range(len(image[index])):
                # add the col_scaleth item to sublist
                if ((j % (col_scale * 3)) // 3) == 0:
                    sublist.append(image[index][j])

            # append sublist into final list
            final_list.append(sublist)
    return final_list

def main():
    input_file = input("Enter an input file:\n")
    output_file = input("Enter an output file:\n")

    in_file = open(input_file, "r")
    out_file = open(output_file, "w")

    # give options for image modification
    print("modifications are:\n\t 1. negate\n\t 2. greyscale \n\t 3. scale")

    # ask for choice of modification
    choice = input("Enter the number of desired modification:\n")
    while choice != "1" and choice != "2" and choice != "3":
        choice = input("Enter the number of desired modification:\n")

    # use negate for choice 1
    if choice == "1":
        # count lines in in_file
        counter = 0
        for line in in_file:
            counter += 1
            # copy the first three header lines
            if counter <= 3:
                out_file.write(line)
            else:
                out_file.write(negate(line))
        return out_file

    # use grayscale function for choice 2
    elif choice == "2":
        # count lines in in_file
        counter = 0
        for line in in_file:
            counter += 1
            # copy the first three header lines
            if counter <= 3:
                out_file.write(line)
            else:
                out_file.write(grey_scale(line))
        return out_file


    # use scale function for choice 3
    else:
        width = int(input("Enter the width scaling factor:\n"))
        height = int(input("Enter the height scaling factor:\n"))
        # count lines in in_file
        counter = 0
        long_list = []
        final_list = []

        for line in in_file:
            counter += 1
            # rewrite the new header file
            if counter <= 3:
                if counter == 2:
                # split file into lines
                    dimension = line.split()
                    # determine width from original file
                    header_width = dimension[0]
                    header_height = dimension[1]
            else:
                # split each line in in_file into lists
                file_lines = line.split()
                # go through element in each line
                for elem in file_lines:
                    long_list.append(int(elem))


        # make a new list to rearrange contents into the right width
        while long_list:
            new_list = []
            for num in range(int(header_width) * 3):
                new_list.append(long_list.pop(0))

            # append the new sublists into a big final list
            final_list.append(new_list)


        # call scale function
        scaled_list = scale(final_list, int(width), int(height))

        # make str to count the columns and rows
        # copy these rows into a str to be copied into new file
        file_str = ""
        rows = 0
        elements = 0

        # for each new list in scaled list, count as one row
        for sublist in scaled_list:
            rows += 1

            # count element in scaled list and add to str
            for elem in sublist:
                elements += 1
                file_str = file_str + str(elem) + " "

            file_str += "\n"

        # count columns in file
        columns = elements // rows // 3

        out_file.write("P3\n" + str(columns) + " " + str(rows) + "\n255\n")
        out_file.write(file_str)

    in_file.close()
    out_file.close()

    return out_file

if __name__ == '__main__':
    # main_part1()  # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1
