# John Deady,2018-01-03
# Iris Data Set
# Adapted from https://en.wikipedia.org/wiki/Iris_flower_data_set to understand the concept.
# This Python script reads the Iris data set in and prints the four numerical values on each row in a nice format. 
# Printed the petal length, petal width, sepal length and sepal width. 
# These values should have the decimal places aligned, with a space between the columns.
# Download Iris Data set. Adapted from http://archive.ics.uci.edu/ml/datasets/Iris
# Used Stackflow to solve this problem



with open(".vscode/iris.data.csv") as x:                 # After downloading the Iris Data set, we open it for x.
    for line in x:                                       # For lines in x
        
        # Print each item (1-4) on all lines with a space beteen each item all aligned
        print(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3])