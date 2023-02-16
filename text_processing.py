"""
    CS051P Lab Assignments: Text Processing

    Name: YUKIE GRACE CHANG
          PINE NETCHARUSSAENG, if pair programming

    Date:   09/29/22

    The goal of this assignment is to familiarize you with processing strings,
    sequences and files, through exercises on looping over contents in string,
    reading and writing files, etc.
"""
from string import *


def every_fourth_char(string):
    """
    prints every fourth character

    :param string: (str) a string
    :return: (str) every fourth character of the string
    """
    return string[::4]


def copy_parts_of_file(old_filename, new_filename):
    """
    reads the specified old file for each line, creates a new line w/every 4th char, writes to the specified new file

    :param old_filename: (str) string of the original file
    :param new_filename: (str) string with every fourth character in old_filename
    :return: (str) string with every fourth character in old_filename created in new_filename
    """
    f_old = open(old_filename, "r")
    f_new = open(new_filename, "w")
    for line in f_old:
        f_new.write(every_fourth_char(line.strip("\n")) + "\n")
    f_old.close()
    f_new.close()


def num_characters(string):
    """
    count and return the number of non-whitespace characters

    :param string: (str) a string
    :return: (int) number of non-whitespace characters
    """
    total = 0
    for char in string:
        if char not in whitespace:
            total = total + 1
    return total


def count_characters(filename):
    """
    for the specified file, counts and returns the total of non-whitespace characters

    :param filename: (str) a file containing string
    :return: (int) number of non-whitespace characters
    """
    total = 0
    outfile = open(filename, "r", encoding="utf-8")
    for line in outfile:
        total = total + num_characters(line)
    print(total)
    outfile.close()


def count_char(string, char):
    # TODO:
    #   1. write a complete docstring for this method
    #   2. write code to
    #      enumerate the chars in string
    #      count number of times specified char appears
    #      whether upper or lower case
    #      return the total number of times
    pass


def num_words(string):
    # TODO:
    #   1. write a complete docstring for this method
    #   2. write code to
    #      enumerate the chars in string
    #      identify and count whitespace separated wrods
    #      return the total number of words
    pass


def main():
    # TODO: implement the following required items
    """
    1. Ask the user for a character to count. If the user does not enter a
       single letter, ask them again. Continue until they enter a character.
    2. Ask the user if they want to run in file or interactive mode by asking
       them to enter a 1 for file mode and a 0 for interactive mode.
    3. If the user is running in interactive mode: ask the user to enter a line
       of text or a -1 if they are done. Continue until the user enters a -1.
    4. If the user is running in file mode: ask the user for a filename.
    5. Print the following set of statistics either about the entered lines
       by the user in interactive mode, or about the file if in file mode:
        a. The total number of lines
        b. The total number of words
        c. The total number of non-whitespace characters
        d. The number of times char appears, ignoring case
        e. The average length of a word (number of non-whitespace characters
           divided by the number of words)
        f. The percentage of char (number of times char appears divided by
           the number of non-whitespace characters, times 100) Note that
           the output should be in the format shown in the sample runs below.
    """
    pass


if __name__ == '__main__':
    main()
