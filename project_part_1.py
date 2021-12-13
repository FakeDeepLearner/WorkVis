""" project_part_1.py - Plotting the Graph

The purpose here is to plot the graph according to the selected industry regarding the data
from before the pandemic (2019) and during the pandemic (2020) the two year will correspond
to 2 different graphs and the x-axis will represent the average working hour while the y-axis
will be representing in the form of year and month.

This module contains all the necessary code to implement the first part of the project, and must be
imported in the main.py file.

"""
import matplotlib.pyplot as plot
import pandas as p
from matplotlib.figure import Figure

during_pandemic_data = p.read_csv('Datasets/during_the_pandemic (1).csv')   
pre_pandemic_data = p.read_csv('Datasets/pre_pandemic.csv')
# Gets the DataFrame from the csv dataset. (Change the input string if the file names or the folder
# names are different.)

industry_and_its_index = {'Agriculture': 0,
                          'Forestry, fishing, mining, quarrying, oil and gas': 1,
                          'Construction': 2,
                          'Wholesale and retail trade': 3,
                          'Transportation and warehousing': 4,
                          'Educational services': 5,
                          'Health care and social assistance': 6,
                          'Accommodation and food services': 7,
                          'Public administration': 8}
# A dictionary so that each industry is connected to the following data set from the DataFrame.


def plotting_the_graph(industry: str) -> Figure:
    """plots the graph based on the industry chosen
    for aesthetic purposes, in the function, the name will be changed so that all word will
    capitalize their first letter.

    E.g: 'Educational services' -> 'Educational Services'

    >>> plotting_the_graph('Agriculture')
    <Figure size 1600x1200 with 2 Axes>
    """

    pre_pandemic_points = points_of_pre_pandemic(industry)
    during_pandemic_points = points_of_during_pandemic(industry)
    # Getting the list of coordinates of the chosen industry as (Month, Average Working Hours)
    # using helper functions.

    industry_name = industry.split(' ')
    industry_name_fixed = [industry_name[0]]
    # Accumulator for the new industry name so that the first alphabet of each word is capitalized,
    # index 0 doesn't count because its first letter is capitalized by default.

    for i in range(1, len(industry_name)):
        if industry_name[i][0].islower() and industry_name[i] != 'and':
            industry_name_fixed.append(industry_name[i].replace(industry_name[i][0],
                                       industry_name[i][0].capitalize(), 1))
        else:
            industry_name_fixed.append(industry_name[i])

    # If the first alphabet of the word is lower cased then change it to upper case,
    # the first word of the industry should always have an uppercase letter

    new_industry_name = ' '.join(industry_name_fixed)

    pre_pandemic_time_axis = []
    pre_pandemic_stat_axis = []
    during_pandemic_time_axis = []
    during_pandemic_stat_axis = []
    # Accumulators for the x and y axis for the 2 graphs.

    for points in pre_pandemic_points:
        time, stat = points
        pre_pandemic_time_axis.append(time)
        pre_pandemic_stat_axis.append(stat)
    for points in during_pandemic_points:
        time, stat = points
        during_pandemic_time_axis.append(time)
        during_pandemic_stat_axis.append(stat)
    # Creating the list of the following x and y axis that matplotlib will use.

    max_y_axis = int(round(max(during_pandemic_stat_axis + pre_pandemic_stat_axis) / 5) * 5)
    min_y_axis = int(round(min(during_pandemic_stat_axis + pre_pandemic_stat_axis) / 5) * 5)
    # Simple algorithm that creates the min/max of y-axis based on the multiple of 5.

    figure, graphs = plot.subplots(2, facecolor='#73C2FB')

    # Declaring that there will be 2 different graphs and its background color.

    graphs[0].set_title(new_industry_name + "'s Average Working Hours Before the Pandemic (2019)")
    graphs[1].set_title(new_industry_name + "'s Average Working Hours During the Pandemic (2020)")
    # Creating the titles for the 2 graphs.

    graphs[0].plot(pre_pandemic_time_axis, pre_pandemic_stat_axis, color='red', marker='o')
    graphs[1].plot(during_pandemic_time_axis, during_pandemic_stat_axis, color='blue', marker='o')
    # Plotting the line graph with distinct color while also plotting each point with a marker.

    plot.setp(graphs, ylabel='Average Working Hours',
              xlabel='Month', ylim=(int(min_y_axis - 5), int(max_y_axis + 5)))

    # Labeling each axis and using the min/max values to indicate the range of the graph's y-axis.
    figure.set_size_inches(16, 12)
    # Setting the window size so it isn't too small.
    figure.tight_layout(pad=3.0)
    # Setting the spacing between 2 graphs

    plot.close('all')
    return figure
    # Return the figure to the main file to update the canvas


def points_of_pre_pandemic(industry: str) -> list[tuple[int, int]]:
    """Returns the list of point from the dataset based on the chosen industry
        based on the average working hour and month before the pandemic

    >>> points_of_pre_pandemic('Agriculture')
    [('19-Jan', 40.2),\
 ('19-Feb', 38.9),\
 ('19-Mar', 40.7),\
 ('19-Apr', 41.7),\
 ('19-May', 47.5),\
 ('19-Jun', 44.2),\
 ('19-Jul', 44.0),\
 ('19-Aug', 44.4),\
 ('19-Sep', 47.6),\
 ('19-Oct', 45.1),\
 ('19-Nov', 43.8),\
 ('19-Dec', 41.5)]
    """
    index = industry_and_its_index[industry]
    before_pandemic = pre_pandemic_data.loc[index].to_dict()
    keys = list(before_pandemic.keys())
    pre_pandemic_points = []

    for month in keys[1:13]:
        pre_pandemic_points.append((month, before_pandemic[month]))

    return pre_pandemic_points


def points_of_during_pandemic(industry: str) -> list[tuple[int, int]]:
    """Returns the list of point from the dataset based on the chosen industry
        based on the average working hour and month during the pandemic

    >>> points_of_during_pandemic('Agriculture')
    [('20-Jan', 38.9),\
 ('20-Feb', 39.0),\
 ('20-Mar', 41.2),\
 ('20-Apr', 42.3),\
 ('20-May', 48.8),\
 ('20-Jun', 45.3),\
 ('20-Jul', 42.7),\
 ('20-Aug', 46.0),\
 ('20-Sep', 49.5),\
 ('20-Oct', 44.6),\
 ('20-Nov', 42.0),\
 ('20-Dec', 38.9)]

    """
    index = industry_and_its_index[industry]
    during_pandemic = during_pandemic_data.loc[index].to_dict()
    keys = list(during_pandemic.keys())
    during_pandemic_points = []

    for month in keys[1:13]:
        during_pandemic_points.append((month, during_pandemic[month]))

    return during_pandemic_points


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas', 'matplotlib.pyplot', 'matplotlib.figure'],
        'max-line-length': 121,
        'max-nested-blocks': 4,
        'disable': ['R1705', 'C0200']
    }
    )

