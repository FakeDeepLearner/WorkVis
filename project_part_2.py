"""
This module contains the code required to operate the second part of the project
"""

from datetime import time
import matplotlib.pyplot as plot
import pandas as p
import project_part_1 as proj1
industries_and_indexes = proj1.industry_and_its_index


pre_pandemic_data = p.read_csv('Datasets/pre_pandemic.csv')
during_the_pandemic_data = p.read_csv('Datasets/during_the_pandemic (1).csv')
print(pre_pandemic_data)
print(pre_pandemic_data.iloc[0, 1])

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
    #Creating a new DataFrame where rows and columns are 0-indexed by default
    new_dataframe = p.DataFrame(columns= ["industry", "timeframe",  "Increase- Decrease", "Percentage of Increase - Decrease"], index= ["values"])
    new_dataframe["industry"] = industry
    dates_to_indexes = {"January 2019- 20": 0, "February 2019- 20": 1,
                        "March 2019- 20": 2, "April 2019- 20": 4,
                        "May 2019- 20": 3, "June 2019- 20": 5,
                        "July 2019- 20": 6, "August 2019- 20": 7,
                        "September 2019- 20": 8, "October 2019- 20": 9,
                        "November 2019- 20": 10, "Decemeber 2019- 20": 11}
    dates = list(dates_to_indexes.keys())


    # The iloc[:, :] function allows us to access specific values from the DataFrame by their indexes. 
    # The first parameter, which is the rows,  takes 2 integers separated by a colon (:) and gives out that part of the data frame. The end point is exclusive.
    # The second parameter, which is the colums,  takes 2 integers separated by a colon (:) and gives out that part of the data frame. The end point is exclusive.
    # For example iloc[4 : 7, 3 : 14] would return the rows 4, 5 and 6; the columns from 3 up to but not including 14.
    
    
    # Considering each case separately.

    new_dataframe["timeframe"] = dates[dates_to_indexes[time_frame]]
    value_1 = during_the_pandemic_data.iloc[industries_and_indexes[industry], dates_to_indexes[time_frame] + 1]
    # Getting the necessary value from during_the_pandemic_data
    value_2 = pre_pandemic_data.iloc[industries_and_indexes[industry], dates_to_indexes[time_frame] + 1]
    # Getting the necessary value from pre_pandemic_data
    new_dataframe["Increase- Decrease"] = value_1 - value_2
    new_dataframe["Percentage of Increase - Decrease"] = 100 * ((value_1 - value_2) / value_2)
    # Getting a percentage

    return new_dataframe
