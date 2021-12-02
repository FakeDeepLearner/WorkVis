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
    
    
    # The iloc[:, :] function allows us to access specific values from the DataFrame by their indexes. 
    # The first parameter, which is the rows,  takes 2 integers separated by a colon (:) and gives out that part of the data frame. The end point is exclusive.
    # The second parameter, which is the colums,  takes 2 integers separated by a colon (:) and gives out that part of the data frame. The end point is exclusive.
    # For example iloc[4 : 7, 3 : 14] would return the rows 4, 5 and 6; the columns from 3 up to but not including 14.
    
    
    # Considering each case separately.
        
    if time_frame == "January 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 1]      # Getting the necessary value from during_the_pandemic_data
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 1]              # Getting the necessary value from pre_pandemic_data
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b    # Getting a percentage
        
    if time_frame == "February 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 2]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 2]              
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame ==  "March 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 3]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 3]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame == "April 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 4]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 4]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame == "May 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 5]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 5]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame == "June 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 6]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 6]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame == "July 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 7]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 7]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame == "August 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 8]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 8]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame == "September 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 9]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 9]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame == "October 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 10]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 10]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame == "November 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 11]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 11]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    if time_frame == "Decemeber 2019- 20":
        new_dataframe["timeframe"] = time_frame
        a = during_the_pandemic_data.iloc[industries_and_indexes[industry], 12]      
        b = pre_pandemic_data.iloc[industries_and_indexes[industry], 12]             
        new_dataframe["Increase- Decrease"] = a - b                                 
        new_dataframe["Percentage of Increase - Decrease"] = (100 * (a - b)) / b 
        
    
    return new_dataframe
    
