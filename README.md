# Programming-Scripting-Project-18
This repository contains a project which focuses on the Fisher's Iris data set. The project requires researching the data set, and then writing documentation and code in the [Python](https://www.python.org/) programming language based on that research. 

### Introduction
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems* as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus.(ref [wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set))

The iris dataset contains measurements for 150 iris flowers from three different species.The three classes in the Iris dataset:
 * Iris-setosa 
 * Iris-versicolor 
 * Iris-virginica 

The four features of the Iris dataset:
 * sepal length in cm
 * sepal width in cm
 * petal length in cm
 * petal width in cm

Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.(ref [wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set))

### Importance of Fisher's Iris Data Set
Fisher's linear discriminant analysis used methods in statistics and pattern recognition to find a linear combination of features which characterizes or separates two or more classes of objects or events. The resulting combination may be used as a linear classifier ([ref](https://pdfs.semanticscholar.org/1ab8/ea71fbef3b55b69e142897fadf43b3269463.pdf))

This lead to the development of machine learning

### Downloading the Iris Data Set
 1. Go to [UCI](https://archive.ics.uci.edu/ml/datasets/iris) 
 2. Click on the Data Folder [link](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)
 3. Click on the [iris.data](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
 4. Copy this to excel and save in a local folder.

### Getting Started
After downloading the Iris data set to excel, We can open this in python. We now need to download open source libraies NumPy, SciPy and Matpotlib(https://pypi.python.org/pypi/numpy). These will help us with scientific computing and technical computing and create graphs and histograms in our analysis of the Iris data set.


[NumPy](http://www.numpy.org/) is the fundamental package for scientific computing with Python. It contains among other things:
 * a powerful N-dimensional array object
 * sophisticated (broadcasting) functions
 * tools for integrating C/C++ and Fortran code
 * useful linear algebra, Fourier transform, and random number capabilities
 
Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

[Matplotlib](https://matplotlib.org/) is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.

[SciPy](https://en.wikipedia.org/wiki/SciPy) is an open-source Python library used for scientific computing and technical computing.
SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering.








numpy etc https://solarianprogrammer.com/2017/02/25/install-numpy-scipy-matplotlib-python-3-windows/




https://www.kaggle.com/uciml/iris
At first sight, Petal length and petal width seem to diverge from the normal distribution - graphs

Histogram

https://www.packtpub.com/mapt/book/big_data_and_business_intelligence/9781782161400/2/ch02lvl1sec14/the-iris-dataset
The Iris dataset is a classic dataset from the 1930s; it is one of the first modern examples of statistical classification.
The setting is that of Iris flowers, of which there are multiple species that can be identified by their morphology. Today, the species would be defined by their genomic signatures, but in the 1930s, DNA had not even been identified as the carrier of genetic information.

 Relevant Information:
   --- This is perhaps the best known database to be found in the pattern
       recognition literature.  Fisher's paper is a classic in the field
       and is referenced frequently to this day.  (See Duda & Hart, for
       example.)  The data set contains 3 classes of 50 instances each,
       where each class refers to a type of iris plant.  One class is
       linearly separable from the other 2; the latter are NOT linearly
       separable from each other.
   --- Predicted attribute: class of iris plant.
   --- This is an exceedingly simple domain.
   --- This data differs from the data presented in Fishers article
	(identified by Steve Chadwick,  spchadwick@espeedaz.net )
	The 35th sample should be: 4.9,3.1,1.5,0.2,"Iris-setosa"
	where the error is in the fourth feature.
	The 38th sample: 4.9,3.6,1.4,0.1,"Iris-setosa"
	where the errors are in the second and third features.  


### References
https://matplotlib.org/
http://www.numpy.org/
https://en.wikipedia.org/wiki/SciPy


### Download the data set and write some Python code
http://sebastianraschka.com/Articles/2014_python_lda.html#introduction

### Summarise the data set by max, min and mean of each using python

### Write a summary of your investigation

### Tables ad graphics
