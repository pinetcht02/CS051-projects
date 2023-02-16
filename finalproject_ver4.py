"""
    CS051P Lab Assignments: Final Project

    Author: Pine Netcharussaeng, Yukie Grace Chang

    Date:   11/30/22
"""
import matplotlib.pyplot as plt

def parse_file(fname):
    """
    changes the file data to correct format for artist and song name columns
    note: there are no songs that have commas in both artists and songs names

    :param fname: csv file containing song data
    :return row_list: list of correctly formatted rows
    """
    # open file
    in_file = open(fname, "r", encoding='utf-8')

    # initialize counter and data_list
    counter = 0
    data_list = []

    # checks the rows in the file if they have quotation marks
    for row in in_file:
        counter += 1

        # checks from second row
        if counter > 1:

            # splits row and creates list
            row_list = row.split(",")

            # goes through artist and song name column in each row
            for column in range(2):
                name = row_list[column]

                # check if first char of song name is a quotation mark
                if name[0] == '"':

                    # initializes name counter
                    name_counter = 0

                    # for each elem in the row
                    for elem in row_list:
                        name_counter += 1

                        # skips first index of the name
                        if name_counter > 1:

                            # checks if last char is quotation mark for that elem
                            if elem[-1] == '"':

                                # updates name column to include till end of quotation mark, deletes duplicates of elem
                                row_list[column] = row_list[column:name_counter]
                                del (row_list[(column + 1):name_counter])

                                # updates name from list to string by merging
                                name = ""
                                for name_parts in row_list[column]:
                                    for char in name_parts:
                                        name += char
                                row_list[column] = name
                                data_list.append(row_list)

                # if both artist and song name are in correct format, add to data_list
                elif column == 1:

                    # append only when the artist name did not contain quotation mark bc if so already appended to list
                    if row_list[0][0] != '"':
                        data_list.append(row_list)

    in_file.close()
    return data_list


def create_dict(data_list, column):
    """
    creates dictionary relating song name and data of interest

    :param data_list: (list) a list of lists containing top 2000 songs information
    :param column: (int) the index of column containing data of interest
    :return: (dict) a dictionary relating desired information
    """
    data_dict = {}

    # create dict correlating song name and desired information
    for i in range(len(data_list)):
        song_name = data_list[i][1]
        variable = data_list[i][column]
        data_dict[song_name] = float(variable)
    return data_dict


def danceability_dict(data_list):
    """
    dictionary correlating song name and danceability of a particular song

    :param data_list: (list) a list of lists containing top 2000 songs information
    :return: (dict) a dictionary containing song name and danceability
    """
    return create_dict(data_list, 6)


def popularity_dict(data_list):
    """
     dictionary correlating song name and popularity of a particular song

     :param data_list: (list) a list of lists containing top 2000 songs information
     :return: (dict) a dictionary containing song name and popularity
     """
    return create_dict(data_list, 5)


def correlate_data(dance_dict, pop_dict):
    """
    correlates data from dance_dict and pop_dict into a list of lists

    :param dance_dict: (dict) a dictionary containing song name and danceability
    :param pop_dict: (dict) a dictionary containing song name and popularity

    :return: a list of lists containing  a song's danceability correlated to that song's popularity
    """
    # create an empty list for the final data set
    co_list = []

    # iterate through song name (key) of dance_dict
    for songname in dance_dict:

        # append danceability and popularity into correlate list
        co_list.append([dance_dict[songname], pop_dict[songname]])

    return co_list


def year_dance_dict(data_list):
    """
    create a dictionary correlating year to average song danceability of that year

    :param data_list: (list) a list of lists containing top 2000 songs information
    :return: (dict) a dictionary containing year to that year's average song danceability
    """
    yr_dance_dict = {}

    # go through data list, index year and danceability from data_list's sublist
    for i in range(len(data_list)):
        year = str(data_list[i][4])
        danceability = str(data_list[i][6])

        # correlate year to danceability
        if year not in yr_dance_dict:
            # create entry of year (key) to hit songs' danceability list (value)
            yr_dance_dict[year] = [float(danceability)]
        else:

            # append danceability into existing list
            yr_dance_dict[year].append(float(danceability))

    # update the danceability list to a single avg danceability of that year
    for each_year in yr_dance_dict:
        # initialize dance_sum
        dance_sum = 0

        # assign variable to danceabilty list for each yr
        dance_list = yr_dance_dict[each_year]

        # sum the value in danceability list of that yr
        for dance in dance_list:
            dance_sum += dance

        # average the danceability sum and update dictionary
        dance_avg = dance_sum / len(dance_list)
        yr_dance_dict[each_year] = [dance_avg]

    return yr_dance_dict


def year_songs(data_list):
    """
    correlate number of hit songs per year into a list

    :param data_list: (list) a list of lists containing top 2000 songs information
    :return: (list) a list containing year to number of hit songs in that year
    """
    ys_dict = {}

    for row in data_list:
        year = row[4]
        # if song is founded in that particular year, add one to that key
        if year not in ys_dict:
            ys_dict[year] = 1
        else:
            ys_dict[year] += 1

    # make a reverse dictionary of num songs (key) to year(s) (value)
    reverse_ys_dict = {}
    for year in ys_dict:
        # create new list containing number of hit songs corresponding to a year
        if ys_dict[year] not in reverse_ys_dict:
            reverse_ys_dict[ys_dict[year]] = [int(year)]
        # if number of song (key) already exists, append the year into that key
        else:
            reverse_ys_dict[ys_dict[year]].append(int(year))

    # make a list of num songs and sort them into order
    num_song_list = []
    for num_song in reverse_ys_dict:
        num_song_list.append(num_song)
    num_song_list.sort()

    # make list containing sorted num of hit songs per year
    sorted_ys_list = []
    counter = 1
    not_top_ten = True
    while not_top_ten:
        # go through num_song_list (list of hit songs per year) backwards
        for i in range(len(num_song_list) - 1, -1, -1):
            counter += 1
            num_song = num_song_list[i]
            year = str(reverse_ys_dict[num_song])

            # append to list containing number of songs per year
            sorted_ys_list.append([num_song, year])

            # iterate 10 times for Top 10
            if counter > 10:
                not_top_ten = False
                return sorted_ys_list


def scatter_plot(datalist):
    """
    creates a scatter plot of popularity and danceability correlation using data from a list of lists

    :param datalist: (list) a list of lists  containing popularity and danceability correlates
    :return: None
    """
    # create two empty lists for x- and y-axis
    x = []
    y = []

    # go through each sublist to add x and y data points
    for sublist in datalist:
        x.append(sublist[1])  # popularity
        y.append(sublist[0])  # danceability

    # create scatter plot, name x- and y-axis and title
    plt.plot(x, y, "b.", "hit songs")

    # label and show graph
    plt.xlabel("popularity")
    plt.ylabel("danceability")
    plt.title("Correlation of Song Popularity and Danceability")
    plt.legend()
    plt.show()


def linear_plot(dict):
    """
    plots a line graph of showing change of danceability over time

    :param dict: (dict) dict containing year and the year's avg song danceability
    """
    # create two empty lists for x- and y-axis
    x = []
    y = []

    # go through dictionary to add x and y data points
    for key in dict:
        x.append(key)  # year

    # sort year into chronological order
    x.sort()

    # append each year's corresponding avg danceability
    for num in x:
        y.append(dict[num])  # avg danceability

    # create line graph, name x- and y-axis and title
    plt.plot(x, y, "top songs")

    # label and show graph
    plt.xlabel("year")
    plt.ylabel("danceability")
    plt.title("Change of Danceability over time")
    plt.legend()
    plt.show()


def bar_graph(data_list):
    """
    creates a bar graph of years producing the most hit songs

    :param data_list: (list) list containing number of hit songs and the correlated year
    :return: None
    """
    x = []
    y = []

    # go through the data list
    for sublist in data_list:
        x.append(sublist[1])  # append year into list of x values
        y.append(sublist[0])  # append song number into list of y values

    # create bar graph
    plt.xlabel("Released year")
    plt.ylabel("Number of hit songs")
    plt.title("Years that produced most number of hit songs")
    plt.bar(x, y, color='maroon', width=0.4)
    plt.xticks(fontsize=8)

    # shows plot value to top of bar
    for index in range(len(x)):
        plt.text(x[index], y[index], y[index])

    plt.show()


def main():
    # CREATE SCATTER PLOT OF SONG DANCEABILITY-POPULARITY CORRELATION
    # parse file into a list with correct format for artist and song name columns
    data_list = parse_file("songs_normalize.csv")

    # make dicts for song-danceability and song-popularity
    dance_dict = danceability_dict(data_list)
    pop_dict = popularity_dict(data_list)

    # correlate data, create scatter plot
    dp_data = correlate_data(dance_dict, pop_dict)
    scatter_plot(dp_data)

    # PLOT CHANGE OVER TIME INTO LINE GRAPH
    yd_dict = year_dance_dict(data_list)
    linear_plot(yd_dict)

    # PLOT BAR GRAPH OF YEARS PRODUCING THE MOST HIT SONGS
    ys_list = year_songs(data_list)
    bar_graph(ys_list)


if __name__ == '__main__':
    main()
