"""
  This module contains all of the required code to run the third part of the project  
"""

import pandas as p
import matplotlib.pyplot as plot
from matplotlib.figure import Figure
import project_part_1 as proj1


pre_pandemic_data = p.read_csv('Datasets/pre_pandemic.csv')
during_the_pandemic_data = p.read_csv('Datasets/during_the_pandemic (1).csv')

industries_and_indexes = proj1.industry_and_its_index


def create_dataframe(industry: str) -> p.DataFrame:
    """
    Create and return a pandas DataFrame with the necessary data
    
    Preconditions:
        - industry in proj1.industry_and_its_index
    """
    new_dataframe = p.DataFrame(columns= ["Industry", "Pre-Pandemic Average", "Average During the Pandemic"], index= ["values"])

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

    if len(industry) > 30:
        industry_name_fixed.insert(len(industry_name) // 2, '\n')

    new_industry_name = ' '.join(industry_name_fixed)

    new_dataframe["Industry"] = new_industry_name

    pre_pandemic_total = 0
    during_the_pandemic_total = 0
    
    # Accumulating the sum of the necessary row, decided by the industry passed in.
    for col_num in range(1, 13): # There are a total of 12 rows, representing each month
        pre_pandemic_total += float(pre_pandemic_data.iloc[industries_and_indexes[industry], col_num])
        during_the_pandemic_total += float(during_the_pandemic_data.iloc[industries_and_indexes[industry], col_num])
    
    new_dataframe["Pre-Pandemic Average"] = pre_pandemic_total / 12
    new_dataframe["Average During the Pandemic"] = during_the_pandemic_total / 12

    return new_dataframe
    

def create_table_value(dataframe: p.DataFrame) -> list[tuple[str, float or str]]:
    """
    Returns the values of the dataframe as a list of tuples.
    """
    new_frame = dataframe.to_dict()
    
    data_list = []
    for item in new_frame:
        data_list.append((item, new_frame[item]['values']))
    
    return data_list


def create_table(industry: str) -> Figure:
    """Creates the table with the data"""

    data = create_table_value(create_dataframe(industry))
    values = [data[i][0] for i in range(len(data))]
    numerics = [str(data[i][1]) for i in range(len(data))]

    figure, tables = plot.subplots(facecolor='#73C2FB')
    tables.set_axis_off()
    table = tables.table(
        cellText=[numerics],
        rowLabels=None,
        colLabels=values,
        loc='upper center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    table.scale(1.25, 1.5)
    figure.set_size_inches(16, 12)

    tables.set_title('Difference in Yearly Average in the industry of ' + data[0][1])

    plot.box(on=None)

    return figure
