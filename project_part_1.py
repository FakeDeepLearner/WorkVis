import matplotlib as mp
import matplotlib.pyplot as plot
import matplotlib.figure as fig
import pandas as p

during_pandemic_data = p.read_csv('during_the_pandemic (1).csv')
pre_pandemic_data = p.read_csv('pre_pandemic.csv')
industry_and_its_index = {'Agriculture': 0,
                          'Forestry, fishing, mining, quarrying, oil and gas': 1,
                          'Construction': 2,
                          'Wholesale and retail trade': 3,
                          'Transportation and warehousing': 4,
                          'Educational services': 5,
                          'Health care and social assistance': 6,
                          'Accommodation and food services': 7,
                          'Public administration': 8}


def plotting_the_graph(industry: str) -> None:
    """plots the graph based on the industry chosen"""

    pre_pandemic_points = points_of_pre_pandemic(industry)
    during_pandemic_points = points_of_during_pandemic(industry)

    pre_pandemic_time_axis = []
    pre_pandemic_stat_axis = []
    during_pandemic_time_axis = []
    during_pandemic_stat_axis = []
    for points in pre_pandemic_points:
        time, stat = points
        pre_pandemic_time_axis.append(time)
        pre_pandemic_stat_axis.append(stat)
    for points in during_pandemic_points:
        time, stat = points
        during_pandemic_time_axis.append(time)
        during_pandemic_stat_axis.append(stat)
    figure, graphs = plot.subplots(2)
    graphs[1].set_title(industry + "'s Average Working Hour During the Pandemic")
    graphs[0].set_title(industry + "'s Average Working Hour Before the Pandemic")

    graphs[0].plot(pre_pandemic_time_axis, pre_pandemic_stat_axis, 'red')
    graphs[1].plot(during_pandemic_time_axis, during_pandemic_stat_axis, 'blue')

    graphs[0].yticks(pre_pandemic_stat_axis)
    graphs[1].yticks(during_pandemic_stat_axis)  # doesn't work for some reason
                                                 

    graphs[0].ylabel('Average Working Hours')
    graphs[1].ylabel('Average Working Hours')

    graphs[0].xlabel('Month')
    graphs[1].xlabel('Month')

    figure.set_size_inches(18.5, 10.5)  # doesn't work (trying to set size for the figure so
                                        # it isn't so small at the beginning)
    plot.show()


def points_of_pre_pandemic(industry: str) -> list[tuple[int, int]]:
    """Returns the point of the dataset based on each industry

    """
    index = industry_and_its_index[industry]
    before_pandemic = pre_pandemic_data.loc[index].to_dict()
    keys = list(before_pandemic.keys())
    pre_pandemic_points = []

    for month in keys[1:13]:
        pre_pandemic_points.append((month, before_pandemic[month]))

    return pre_pandemic_points


def points_of_during_pandemic(industry: str) -> list[tuple[int, int]]:
    """Returns the point of the dataset based on each industry

    """
    index = industry_and_its_index[industry]
    during_pandemic = during_pandemic_data.loc[index].to_dict()
    keys = list(during_pandemic.keys())
    during_pandemic_points = []
    for month in keys[1:13]:
        during_pandemic_points.append((month, during_pandemic[month]))

    return during_pandemic_points
