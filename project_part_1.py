import matplotlib as mp
import matplotlib.pyplot as plot
import pandas as p
from tkinter import *
during_pandemic_data = p.read_csv('Datasets/during_the_pandemic (1).csv')
pre_pandemic_data = p.read_csv('Datasets/pre_pandemic.csv')
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

    graphs[0].plot(pre_pandemic_time_axis, pre_pandemic_stat_axis, color='red', marker='o')
    graphs[1].plot(during_pandemic_time_axis, during_pandemic_stat_axis, color='blue', marker='o')

    plot.ylabel('Average Working Hours')
    plot.xlabel('Month')
    figure.set_size_inches(10, 7)
    plot.ylim([25, 50])
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




root = Tk()


my_button = Button(root, text = "Agriculture", command= plotting_the_graph("Agriculture"), padx= 40, pady=1)
my_button.grid(row = 0, column= 0)

my_button1 = Button(root, text = "FFMQOG", command= plotting_the_graph('Forestry, fishing, mining, quarrying, oil and gas'), padx= 40, pady=1)
my_button1.grid(row = 0, column= 1)

my_button2 = Button(root, text = "Construction", command= plotting_the_graph('Construction'), padx= 40, pady=1)
my_button2.grid(row = 0, column= 2)

my_button3 = Button(root, text = "Wholesale and retail", command= plotting_the_graph('Wholesale and retail trade'), padx= 40, pady=1)
my_button3.grid(row = 0, column= 3)

my_button4 = Button(root, text = "Transportation", command= plotting_the_graph('Transportation and warehousing'), padx= 40, pady=1)
my_button4.grid(row = 0, column= 4)

my_button5 = Button(root, text = "Education", command= plotting_the_graph('Educational services'), padx= 40, pady=1)
my_button5.grid(row = 0, column= 5)

my_button6 = Button(root, text = "HC & SA", command= plotting_the_graph('Health care and social assistance'), padx= 40, pady=1)
my_button6.grid(row = 0, column= 6)

my_button7 = Button(root, text = "A & Food Services", command= plotting_the_graph('Accommodation and food services'), padx= 40, pady=1)
my_button7.grid(row = 0, column= 7)

my_button8 = Button(root, text = "Public administration", command= plotting_the_graph('Public administration'), padx= 40, pady=1)
my_button8.grid(row = 0, column= 8)

root.mainloop()