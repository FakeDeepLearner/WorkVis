"""
This module contains the code required to operate the second part of the project
"""

from datetime import time
from tkinter.constants import CENTER
import matplotlib.pyplot as plot
import pandas as p
import project_part_1 as proj1
from matplotlib.figure import Figure

industries_and_indexes = proj1.industry_and_its_index  # The dictionary corresponding to the industries

pre_pandemic_data = p.read_csv('Datasets/pre_pandemic.csv')
during_the_pandemic_data = p.read_csv('Datasets/during_the_pandemic (1).csv')


def create_dataframe(industry: str, time_frame: str) -> p.DataFrame:
    """
    Create and return a new pandas dataframe

    Preconditions:
        - timeframe in ["January 2019- 20", "February 2019- 20", "March 2019- 20",
                "April 2019- 20", "May 2019- 20", "June 2019- 20",
               "July 2019- 20", "August 2019- 20", "September 2019- 20",
                "October 2019- 20", "November 2019- 20", "Decemeber 2019- 20"]

        - industry in proj1.industry_and_its_index
    """
    # Creating a new DataFrame where rows and columns are 0-indexed by default
    new_dataframe = p.DataFrame(columns=["Industry", "Time Frame", "Pre-Pandemic Value", "Value During the Pandemic",
                                         "Increase- Decrease", "Percentage of Increase - Decrease"], index=["values"])
    new_dataframe["Industry"] = industry

    dates_to_indexes = {"January 2019- 20": 0, "February 2019- 20": 1,
                        "March 2019- 20": 2, "April 2019- 20": 3,
                        "May 2019- 20": 4, "June 2019- 20": 5,
                        "July 2019- 20": 6, "August 2019- 20": 7,
                        "September 2019- 20": 8, "October 2019- 20": 9,
                        "November 2019- 20": 10, "Decemeber 2019- 20": 11}

    dates = list(dates_to_indexes.keys())

    # The iloc[:, :] function allows us to access specific values from the DataFrame by their indexes.
    # The first parameter, which is the rows,  takes 2 integers separated by a colon (:) and gives out that part of the data frame. The end point is exclusive.
    # The second parameter, which is the colums,  takes 2 integers separated by a colon (:) and gives out that part of the data frame. The end point is exclusive.
    # For example iloc[4 : 7, 3 : 14] would return the rows 4, 5 and 6; the columns from 3 up to but not including 14.

    new_dataframe["Time Frame"] = dates[dates_to_indexes[time_frame]]  # Modifying the "timeframe" column

    value_1 = during_the_pandemic_data.iloc[industries_and_indexes[industry], dates_to_indexes[time_frame] + 1]
    # Getting the necessary value from during_the_pandemic_data
    value_2 = pre_pandemic_data.iloc[industries_and_indexes[industry], dates_to_indexes[time_frame] + 1]
    # Getting the necessary value from pre_pandemic_data

    new_dataframe["Pre-Pandemic Value"] = value_2
    new_dataframe["Value During the Pandemic"] = value_1

    new_dataframe["Increase- Decrease"] = value_1 - value_2

    new_dataframe["Percentage of Increase - Decrease"] = 100 * ((value_1 - value_2) / value_2)
    # Getting a percentage

    return new_dataframe


def create_table_value(df: p.DataFrame) -> list[tuple[str, float]]:
    """Returns the value of a DataFrame into a list of tuples"""
    df_to_dict = df.to_dict()

    data_list = []
    for item in df_to_dict:
        data_list.append((item, df_to_dict[item]['values']))

    return data_list


def create_table(industry: str, time_frame: str) -> Figure:
    """Creates the table with the data"""

    data = create_table_value(create_dataframe(industry, time_frame))
    values = [data[i][0] for i in range(len(data))]
    numerics = [str(data[i][1]) for i in range(len(data))]

    figure, tables = plot.subplots(facecolor='#73C2FB')
    tables.set_axis_off()
    table =tables.table(
        cellText=[numerics],
        rowLabels=None,
        colLabels=values,
        loc='upper center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    figure.set_size_inches(16, 12)

    tables.set_title('Difference in Percentage Pre and During Pandemic')

    plot.box(on=None)
    plot.show()
    return figure


def plotting_the_table(data: p.DataFrame) -> None:
    """Creates table with data from create_dataframe"""
    
    values = data.values
    # creates an array of values from dataframe

    column_labels = ['Industry', 'date', 'Pre Pandemic Value', 'Pandemic Value',
                     'Difference in revenue in Billions of Dollars' 'Percentage change']
    row_labels = ['Values']
    table_values = values
    # having some issues with turning the specific datatype from create_dataframe to a table as the most simple numpy
    # datatype is int64  but create_dataframe returns a type 0 datatype. I will figure it out by tomorrow

    center = plot.subplot2grid((2, 2), (0, 0), colspan=3, rowspan=4)
    center.table(cellText=table_values,
                 rowLabels=row_labels,
                 colLabels=column_labels, loc="lower center")

    center.axis("off")




