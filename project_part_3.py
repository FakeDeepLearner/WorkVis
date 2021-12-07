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
    
    new_dataframe["Industry"] = industry
    pre_pandemic_total = 0
    during_the_pandemic_total = 0
    
    # Accumulating the sum of the necessary row, decided by the industry passed in.
    for col_num in range(1, 13): # There are a total of 12 rows, representing each month
        pre_pandemic_total += float(pre_pandemic_data.iloc[industries_and_indexes[industry], col_num])
        during_the_pandemic_total += float(during_the_pandemic_data.iloc[industries_and_indexes[industry], col_num])
    
    new_dataframe["Pre-Pandemic Average"] = pre_pandemic_total / 12
    new_dataframe["Average During the Pandemic"] = during_the_pandemic_total / 12
    
    
    return new_dataframe
    


