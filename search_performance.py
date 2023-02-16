"""
    CS051P Lab Assignments: Search Performance

    Author: Pine Netcharussaeng

    Date:   11/3/22

    The goal of this assignment is to implement a few basic search
    algorithms and measure their performance.  As such, it is also
    an introduction to algorithmic complexity.
"""
import random
import time
import csv


def list_of_integers(size):
    """
    creates a list of random integer between 1 and 2*size with the specified number

    :param size: (int) the specified number of random numbers
    :return: (list) a list of random integers
    """

    list = []
    for num in range(size):
        rand_int = random.randint(1, 2*size)
        list.append(rand_int)

    return list


def linear_search(alist, value):
    """
    search list for specified value

    :param alist: (list) a list of integers
    :param value: (int) the number we want to find in the list
    :return: (int) either the index of our desired number or -1
    """

    for i in range(len(alist)):
        if alist[i] == value:
            return i
    return -1


def binary_search_helper(alist, value, start, end):
    """
    a helper function to search for desired number

    :param alist: (list) the list of integers
    :param value: (int) a number we want to search in the list
    :param start: (int) the index of our starting number
    :param end: (int) the index of our last number
    :return: (int) either the index of our desired number or -1
    """

    middle = start + int((end - start) / 2)

    if alist[middle] == value:
        return middle
    elif (end - start) < 2:
        return - 1
    elif alist[middle] > value:
        return binary_search_helper(alist, value, start, middle)
    elif alist[middle] < value:
        return binary_search_helper(alist, value, middle, end)



def binary_search(alist, value):
    """
    search list for specified value through binary method

    :param alist: (list) the list of integers
    :param value: (int) a number we want to search in the list
    :return: (int) either the index of our desired number or -1
    """

    return binary_search_helper(alist, value, 0, len(alist))


def main_part1():
    """
    creates list of random integers, sort the list, and search for values using linear and binary search

    :return: None
    """


    random_list = list_of_integers(3)
    # search for number in the list using linear search
    linear_search(random_list, 2)

    # search for number not in the list using linear search
    linear_search(random_list, 0)
    linear_search(random_list, 7)

    # search for number in the list using binary search
    list.sort(random_list)
    binary_search(random_list, 3)

    # search for number not in the list using binary search
    binary_search(random_list, 0)



# the following functions are to be implemented in part 2

def sorted_comparison(min_size, max_size):
    """
    create and sort lists of different lengths, time functions linear_search and binary_search

    :param min_size: (int) the starting size of list
    :param max_size: (int) the ending size of list
    :return: (list) the list of size, linear time, and binary time
    """

    # initialize main list to report run time
    main_list = []

    # generate lists, starting with min size and increasing to max size
    while min_size <= max_size:

        # generate and sort list
        sorted_list = list_of_integers(min_size)
        sorted_list.sort()

        # search for elem not in list and time linear_search
        start = time.time()
        linear_search(sorted_list, 0)
        end = time.time()
        linear_time = end - start
    
        # search for elem not in list and time binary_search
        start = time.time()
        binary_search(sorted_list, 0)
        end = time.time()
        binary_time = end - start

        # append sublist into the main list
        main_list.append([min_size, linear_time, binary_time])
        min_size = min_size * 2

    return main_list


def unsorted_comparison(min_size, max_size):
    """
    create unsorted lists of different lengths, time functions linear_search and binary_search

    :param min_size: (int) the starting size of list
    :param max_size: (int) the ending size of list
    :return: (list) the list of size, linear time, and binary time
    """

    # initialize main list to report run time
    main_list = []

    # generate lists, starting with min size and increasing to max size
    while min_size <= max_size:

        # generate and sort list
        unsorted_list = list_of_integers(min_size)
        min_size = min_size * 2

        # search for elem not in list and time linear_search
        start = time.time()
        linear_search(unsorted_list, 0)
        end = time.time()
        linear_time = end - start

        # sort list, search for elem not in list, and time binary_search
        start = time.time()
        list.sort(unsorted_list)
        binary_search(unsorted_list, 0)
        end = time.time()
        binary_time = end - start

        # append sublist into the main list
        main_list.append([min_size, linear_time, binary_time])

    return main_list


def main():
    """
    open and write csv file containing runtime data for linear_search and binary search

    :return: None
    """

    # open a csv file to write sorted list
    sorted_file = open("sorted.csv", "w")
    unsorted_file = open("unsorted.csv", "w")

    # write run time of linear and binary function onto sorted_file
    writer = csv.writer(sorted_file)
    runtime_sorted = sorted_comparison(2, 1048576)

    # write each sublist into file
    for sublist in runtime_sorted:
        writer.writerow(sublist)

    # write run time of linear and binary function onto unsorted_file
    writer = csv.writer(unsorted_file)
    runtime_unsorted = unsorted_comparison(2, 1048576)

    # write each sublist into file
    for sublist in runtime_unsorted:
        writer.writerow(sublist)

    return



if __name__ == "__main__":
    main()            # un-comment for part 2
    # main_part1()        # comment out for part 2
