import matplotlib.pyplot as plot
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

    industry_name = industry.split(' ')
    industry_name_fixed = [industry_name[0]]
    for i in range(len(industry_name)):
        if industry_name[i][0].islower():
            industry_name_fixed.append(industry_name[i].replace(industry_name[i][0],
                                        industry_name[i][0].capitalize(), 1))

    new_industry_name = ' '.join(industry_name_fixed)

    for points in pre_pandemic_points:
        time, stat = points
        pre_pandemic_time_axis.append(time)
        pre_pandemic_stat_axis.append(stat)
    for points in during_pandemic_points:
        time, stat = points
        during_pandemic_time_axis.append(time)
        during_pandemic_stat_axis.append(stat)

    max_y_axis = int(round(max(during_pandemic_stat_axis + pre_pandemic_stat_axis) / 5) * 5)
    min_y_axis = int(round(min(during_pandemic_stat_axis + pre_pandemic_stat_axis) / 5) * 5)

    figure, graphs = plot.subplots(2)
    graphs[1].set_title(new_industry_name + "'s Average Working Hour During the Pandemic (2020)")
    graphs[0].set_title(new_industry_name + "'s Average Working Hour Before the Pandemic (2019)")

    graphs[0].plot(pre_pandemic_time_axis, pre_pandemic_stat_axis, color='red', marker='o')
    graphs[1].plot(during_pandemic_time_axis, during_pandemic_stat_axis, color='blue', marker='o')

    plot.setp(graphs[0], ylabel='Average Working Hours',
              xlabel='Month', ylim=(int(min_y_axis - 5), int(max_y_axis + 5)))
    plot.setp(graphs[1], ylabel='Average Working Hours',
              xlabel='Month', ylim=(int(min_y_axis - 5), int(max_y_axis + 5)))
    figure.set_size_inches(16, 10)

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
