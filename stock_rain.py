"""
    CS051P Lab Assignments: Stock v.s. Rain

    Author: Pine Netcharussaeng

    Date:   11/10/22

    The goal of this assignment is to familiarize you with data analysis
    and visualization. You'll practice handling files in csv format,
    create and manipulate Python dictionaries, and do some basic plotting
    using the matplotlib package.
"""
import matplotlib.pyplot as plt
def date_change(string):
    """
    change date format into YYYY-MM-DD

    :param string: (string) a string of a date
    """

    # split date into element in a list
    date_list = string.split("/")

    # initialize empty string
    new_date = ""

    # assign name to each element
    year = date_list[2]
    month = date_list[0]
    day = date_list[1]

    # add 20 to year if year is two-digit
    year = "20" + year

    # add zero to single digit month
    if len(month) < 2:
        month = "0" + month
    else:
        month = month

    # add zero to single digit month
    if len(day) < 2:
        day = "0" + day
    else:
        day = day

    # make a new string with YY-MM-DD format
    new_date = str(year) + "-" + str(month) + "-" + str(day)

    return new_date

def parse_rainfall(fname):
    """
    parse csv file into dictionary, containing date and precipitation level

    :param fname: (file) a csv file containing data on rainfall
    """
    # open file and initialize counter and dictionary list
    f_in = open(fname, "r")
    counter = 0
    parsed_data = {}

    # start writing into dictionary after first line
    for line in f_in:
        counter += 1
        if counter > 1:
            # convert each line into a list
            temp_list = line.split(",")
            # add date and precipitation into dictionary
            for i in range(len(temp_list)):
                if len(temp_list) == 5 and temp_list[1] != '"NA"':
                    date = temp_list[0].strip('"')
                    pcip = temp_list[1]
                    parsed_data[date] = float(pcip)

    f_in.close()
    return parsed_data

parse_rainfall("csvs/rainTest.csv")


def parse_stock(fname, sym):
    """
    parse stock data into dictionary file that contains date and change in stock price

    :param fname: (file) a file containing stock data
    :param sym: (string) the name of the specified stock symbol
    """
    # open file and initialize counter and dictionary list
    f_in = open(fname, "r")
    counter = 0
    parsed_stock = {}

    # start writing into dictionary after first header line
    for line in f_in:
        counter += 1
        if counter > 1:
            # convert each line into a list
            line = line.rstrip("\n")
            temp_list = line.split(",")

            # write only when the list has seven elements, stock sym is same as what is specified, and there is data in
            # opening and closing price entry
            if len(temp_list) == 7 and temp_list[6] == sym and temp_list[1] != '' and temp_list[4] != '':
                # change date into YY-MM-DD format
                date = temp_list[0]
                new_date = date_change(date)

                # find price change in day
                open_price = temp_list[1]
                close_price = temp_list[4]
                price_change = float(close_price) - float(open_price)
                parsed_stock[new_date] = round(price_change, 2)

    f_in.close()
    return parsed_stock


def correlate_data(stock_dict, rain_dict):
    """
    correlates data from stock_dict and rain_dict into a list of lists

    :param stock_dict: (dict) a dictionary containing information of date and stock price change
    :param rain_dict: (dict) a dictionary containing information of date and rainfall levels
    """

    # create an empty list for the final data set
    data_list = []

    # convert dictionary keys into list
    stock_dates = list(stock_dict.keys())
    rain_dates = list(rain_dict.keys())

    # go through both lists and identify dates that are the same
    for stock_key in stock_dates:
        for rain_key in rain_dates:

            # if dates are the same, create list with stock and rainfall data, respectively
            if stock_key == rain_key:
                data_list.append([stock_dict[stock_key], rain_dict[rain_key]])

    return data_list


def scatter_plot(data, format, name, done):
    """
    plots a scatter plot graph of rainfall and stock price correlation

    :param data: (list) data where each entry is a list of 2
    :param format: (string) a matplotlib format string
    :param name: (string) the name of stock whose data is being passed in
    :param done: (boolean) a boolean that is true if and only if this is the last plot
    """
    # create two empty lists for x- and y-axis
    x = []
    y = []
    # plotted_symbols = []

    # go through each sublist to add x and y data points
    for sublist in data:
        x.append(sublist[1])
        y.append(sublist[0])

    # create scatter plot, name x- and y-axis and title
    plt.plot(x, y, format, label=name)

    # only show the graph when this is the last plot
    if done:
        plt.xlabel("rainfall")
        plt.ylabel("stock price change")
        plt.title("Rainfall vs Price Change")
        plt.legend()
        plt.show()



def main():
    """
    ask for user input for rain fall and two stock files, parse and correlate data, and create a graph
    """
    # ask user for rain file and stock file
    rain_input = input("Enter the name of the rainfall data file:\n")
    stock_input = input("Enter the name of the stock data file:\n")

    # START FIRST PLOT
    # ask for first stock symbol
    first_sym = input("Enter a first stock symbol (e.g. MSFT or AMZN):\n")

    # parse rain data and stock data from csv file into dictionary format
    rain_data = parse_rainfall(rain_input)
    stock_data1 = parse_stock(stock_input, first_sym)

    # correlate first stock data and rain data into list and plot
    stock1_rain = correlate_data(stock_data1, rain_data)
    scatter_plot(stock1_rain, "b.", first_sym, False)

    # START SECOND PLOT
    # ask for second stock symbol
    second_sym = input("Enter a second stock symbol (not head-quartered in Seattle):\n")

    # parse second stock data from csv file into dictionary format
    stock_data2 = parse_stock(stock_input, second_sym)

    # correlate first stock data and rain data into list and plot
    stock2_rain = correlate_data(stock_data2, rain_data)
    scatter_plot(stock2_rain, "r+", second_sym, True)


if __name__ == '__main__':
    main()
