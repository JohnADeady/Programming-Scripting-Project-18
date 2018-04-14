# John Deady 2018-04-13
# Analysis of the Iris Dataset

# Import the appropriate Libraries needed for this analysis
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)
import pandas as pd

# Read data file into array
data = pd.read_csv('project/Iris.data.csv')
print (data.head(5))   # Prints the top 5 lines the the data
print (data.tail(5))   # Prints the bottom 5 lines of the data

# This will list all types of species without repeating same species
species = list(data["species"].unique())
print("Types of species: %s\n" % species)

# The lenght of data to be analysis 
print("Dataset length: %i\n" % len(data))

# Print the min and max for each category
print("Sepal length range: [%s, %s]" % (min(data["sepal_length"]), max(data["sepal_length"])))
print("Sepal width range:  [%s, %s]" % (min(data["sepal_width"]), max(data["sepal_length"])))
print("Petal length range: [%s, %s]" % (min(data["petal_length"]), max(data["petal_length"])))
print("Petal width range:  [%s, %s]\n" % (min(data["petal_width"]), max(data["petal_width"])))

#Prin the mean of each category
print("Sepal length mean:\t %f" % np.mean(data["sepal_length"]))
print("Sepal width mean: \t %f" % np.mean(data["sepal_width"]))
print("Petal length mean:\t %f" % np.mean(data["petal_length"]))
print("Petal width mean: \t %f\n" % np.mean(data["petal_width"]))

# Print the standard deviation of each category
print("Sepal length stddev:\t %f" % np.std(data["sepal_length"]))
print("Sepal width stddev: \t %f" % np.std(data["sepal_width"]))
print("Petal length stddev:\t %f" % np.std(data["petal_length"]))
print("Petal width stddev: \t %f\n" % np.std(data["petal_width"]))
