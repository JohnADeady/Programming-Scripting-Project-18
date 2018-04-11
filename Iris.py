# John Deady, 2018-04-08
# Analysis of the  Iris Data Set
# Downloading the appropriate the libaries for this analysis

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)       # Color codes can be set through the high-level seaborn style manager.
import pandas as pd

# Read the file into the array
dataset = pd.read_csv('project/Iris.data.csv')
dataset.head(5)                 # This is the top 5 lines of the Iris Data Set
dataset.tail(5)                 # This is the bottom 5 lines of the Iris Data Set


