# John Deady, 2018-04-08
# Analysis of the  Iris Data Set

with open(".vscode/iris.data.csv") as x:                 # After downloading the Iris Data set, we open it for x.
    for line in x:                                       # For lines in x
        
        # Print each item (1-4) on all lines with a space beteen each item all aligned
        print(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3])



import numpy 
import matplotlib.pyplot as pl

# Read the file into array
data = numpy.genfromtxt('project/iris.data.csv', delimiter= ',')
sepalL = data[:,0]   # Fist column is sepal lenght
sepalW = data[:,1]   # Second column is sepal width
petalL = data[:,2]   # Third column is petal lenght
petalW = data[:,3]   # Fourth column is petal width

#Calculates the mean for each column
meansepalL = numpy.mean(data[:,0])
meansepalW = numpy.mean(data[:,1])
meanpetalL = numpy.mean(data[:,2])
meanpetalW = numpy.mean(data[:,3])

#This will print the mean for each column
print ("Average of the Sepal Length",meansepalL)
print ("Average of the Sepal Width",meansepalW)
print ("Average of the Petal Length",meanpetalL)
print ("Average of the Petal Width",meanpetalW)

#Calculates the smallest in each column
minsepalL = numpy.min(data[:,0])
minsepalW = numpy.min(data[:,1])
minpetalL = numpy.min(data[:,2])
minpetalW = numpy.min(data[:,3])

# This will print the smallest in each column
print ("Smallest Sepal Length",minsepalL)
print ("Smallest Sepal Width",minsepalW)
print ("Smallest Petal Length",minpetalL)
print ("Smallest Petal Width",minpetalW)

#Calculates the largest in each column
maxsepalL = numpy.max(data[:,0])
maxsepalW = numpy.max(data[:,1])
maxpetalL = numpy.max(data[:,2])
maxpetalW = numpy.max(data[:,3])

# This will print the largest in each column
print ("Largest Sepal Length",maxsepalL)
print ("Largest Sepal Width",maxsepalW)
print ("Larget Petal Length",maxpetalL)
print ("Largest Petal Width",maxpetalW)


