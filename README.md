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

![](https://diwashrestha.com/wp-content/uploads/2017/09/images.jpg)


### Importance of Fisher's Iris Data Set
Fisher’s Iris flower data set became a staple of the computing world, especially for testing purposes. The Iris dataset is deservedly widely used throughout statistical science, especially for illustrating various problems in statistical graphics, multivariate statistics and machine learning.

The reason why this is widely used for testing purposes:
* It contains 150 observations, it is small but not trivial.
* The task it poses of discriminating between three species of Iris from measurements of their petals and sepals is simple but challenging.
* The data is real data, of good quality. In principle and in practice, test datasets could be synthetic and that might be necessary or useful to make a point.[ref](https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching)
	

### Getting Started
##### Downloading the Iris Data Set
 1. Go to [UCI](https://archive.ics.uci.edu/ml/datasets/iris) 
 2. Click on the Data Folder [link](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)
 3. Click on the [iris.data](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
 4. Copy this to excel and save in a local folder.
 
 
##### Installing Downloads
[Python](https://www.python.org/) is receommended to run these programs. In order to get started we must download [Anaconda](https://www.anaconda.com/download/) and then [VS Code](https://code.visualstudio.com/).

[Anaconda](https://www.anaconda.com/download/) is a free and open source distribution of the Python and R programming languages for large-scale data processing, predictive analytics, and scientific computing, that aims to simplify package management and deployment.

[VS Code](https://code.visualstudio.com/). is a source code editor developed by Microsoft for Windows, Linux and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring. (ref Wikipedia)

Step by sted guide for downloading [Python](https://www.python.org/)
 1. Open [Python](https://www.python.org/)
 2. Download version Python [3.6.5](https://www.python.org/downloads/)
 3. Follow the instructions on screen - unsure about settings accept the default settings.
 
Step by sted guide for downloading [Anaconda](https://www.anaconda.com/download/):
1. Open Anaconda Download
2. Click Python 3.6 version
3. Follow the instructions on screen - unsure about settings accept the default settings.
4. Once completed test installation

Step by sted guide for downloading [VS Code](https://code.visualstudio.com/)
1. Open VS Studio Download
2. Depending on your OS system - click the appropriate one ie Windows, Mac.
3. Follow the instructions on screen - unsure about settings accept the default settings.
4. Once completed run a simple program 






[NumPy](http://www.numpy.org/) is the fundamental package for scientific computing with Python. It contains among other things:
 * a powerful N-dimensional array object
 * sophisticated (broadcasting) functions
 * tools for integrating C/C++ and Fortran code
 * useful linear algebra, Fourier transform, and random number capabilities
 
Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

[Matplotlib](https://matplotlib.org/) is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.

[SciPy](https://en.wikipedia.org/wiki/SciPy) is an open-source Python library used for scientific computing and technical computing.
SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering.	

[pandas](https://pandas.pydata.org/) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.



![](Head.JPG)
![](Tail.JPG)


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

https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset

https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset

https://rpubs.com/mculp/290780

https://plot.ly/ipython-notebooks/principal-component-analysis/

https://www.neuraldesigner.com/learning/examples/iris_flowers_classification

https://en.wikipedia.org/wiki/Iris_flower_data_set

https://www.techopedia.com/definition/32880/iris-flower-data-set

### Download the data set and write some Python code
http://sebastianraschka.com/Articles/2014_python_lda.html#introduction

### Summarise the data set by max, min and mean of each using python

### Write a summary of your investigation

### Tables ad graphics

### Acknowledge 
