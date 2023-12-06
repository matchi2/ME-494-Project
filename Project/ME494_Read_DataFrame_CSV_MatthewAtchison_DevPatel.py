# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:20:19 2023

@author: Matthew Atchison and Dev Patel

specifically for loading in our X dataframe so that it can be better visualized using Spyder.

"""

import os
import pandas as pd

# This needs to be changed depending on where you save the project folder.
os.chdir(r'C:\Users\Matthew Atchison\OneDrive - University of Illinois Chicago\School\Fall 2023\ME 494\Project\XDataFrameCSVs')

X_DataFrame = pd.read_csv('X_DataFrame_1700267246_4629407.csv', index_col = 0)