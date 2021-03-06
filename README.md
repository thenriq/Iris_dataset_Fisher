# Programing and Scripting GMIT

## The Fisher's Iris Dataset

<br/>

Final Project for the module **Programing and Script** *(H.Dip. in Data Analytics 2020)*

<br/>

Author: **Thiago Henrique Leao de Lima**

<br/><br/>

# Table of Contents
- [Introduction](#introduction)
  - [What is the Iris Flower Dataset](#what-is-the-iris-flower-dataset)
  - [Research](#research)
    - [Who was Ronald Fisher](#who-was-ronald-fisher)
    - [Why was this data collected](#why-was-this-data-collected)
    - [Collection Method](#collection-method)
- [Dataset Analysis](#dataset-analysis)
  - [Pre-requisites and instructions](#pre-requisites-and-instructions)
  - [About this Project](#about-this-project)
  - [How to run the script](#how-to-run-the-script-analysispy)
    - [Script results and outputs](#script-results-and-outputs)
    - [Analysing the results](#analysing-the-results)
- [Final Notes](#final-notes)
- [References](#references)
  
    

   
<br/>
<br/>

# Introduction

## What is the Iris Flower Dataset 

The **IRIS FLOWER DATA SET** is a classic data set introduced by **Ronald Fisher** in 1930. It is used in statistics methods and machine learning and consists of four continuous characters for three species of Iris: *IRIS SETOSA*, *IRIS VERSICOLOR* and *IRIS VIRGINICA*. This characters are **SEPAL LENGTH**, **SEPAL WIDTH**, **PETAL LENGTH** and **PETAL WIDTH**. It contains 150 objects of three different classes, with 50 numeric set values in cm for each class, which one is linearly separable from the other classes, while the other classes are not linearly separable from each other. This data set is available for download from *UC Irvine Machine Learning Repository*[1]

The species in the Iris flower dataset are distributed on the range below:

From *position 1 to position 50*: **IRIS SETOSA**

From *position  51 to position100*: **IRIS VERSICOLOR**

From *position 101 to position 150*: **IRIS VIRGINICA**

<br/>

## Research

This dataset was introduced by the British statistician and biologist **Ronald Fisher** in his 1936 paper *"The use of multiple mesurements in Taxonomic problems  as an example of linear discriminant analysis"* [2 and 3]

### Who was Ronald Fisher

***Image 1.***

![Ronald Fisher](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/Youngfisher.JPG)

<p align="left">
   Sir Ronald Aylmer Fisher, British statistician and geneticist (February 17, 1980 - July 29, 1962) - image from 4
</p>

<br/>

Sir Ronald Aylmer Fisher was one of the most brilliant scientists from the 20th century, considered the greatest biologist since Charles Darwin. His lifework with genetic and statistics made him be described as "a genius who almost single-handedly created the foundations for modern statistical science" and "the single most important figure in 20th century statistics".
He was also awarded as a **Fellow of the Royal Society (FRM)** [5] and made a **Knight Bachelor** by *Queen Elizabeth II* in 1952. In 1958, we was awarded with the **Linnean Society of London Darwin-Wallace Medal**

<br/><br/>

### Why was this data collected

This information was collected by **Edgar Anderson** for his publication in 1936[6]  as it seemed to be an ideal study case about genetic variation and test hypotheses of intra  morphological variation. **Iris versicolor** seems to be a mix between *Iris virginica* and *iris setosa*, which might indicate a case of hybridisation between these two species[8]

<br/>

***Image 2.***

<p align="left">
   <img src="images/irises.png" width=721 height=322>
</p>

<br/><br/>

### Collection method

*Iris setosa* and *Iris versicolor* data were collected in the Gaspé Peninsula *"all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"[7]*  and then published by **Edgar Anderson** in *1935*[8]. The same method was certainly applied for *Iris virginica* before Edgar shared this data with the British statistician and biologist Ronald Aylmer Fisher in 1937[9] 

<br/>

<br/>

***Image 3.***

<p align="left">
   <img src="images/Edgar_Anderson.jpg" width=285 height=383>
</p>
<p align="left">
Edgar Shannon Anderson, american botanist  (November 9, 1897 – June 18, 1969). Image from 9
</p>

<br/><br/>

# Dataset Analysis
## Pre-requisites and instructions
<br/>
Requirements to successfully run the scripts on this project is to have the Python interpreter installed on a computer. Steps on how to download and install Python can be obtained from the link https://www.python.org/downloads

<br/>

Also, a number of libraries must be installed and imported before running this script. The libraries install process can be done from the Command prompt (cmd). 

Steps to install libraries:

**Seaborn**: *pip install seaborn*

**Pandas**: *pip install pandas*

**Matplotlib**: *pip install matplotlib*

<br/>

**Seaborn** - *Seaborn* is a Python data visualization library based on *matplotlib*. It provides a high-level interface for drawing attractive and informative statistical graphics.

**Pandas** - *Pandas* is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.

**Matplotlib** - *Matplotlib* is a comprehensive library for creating static, animated, and interactive visualizations in Python.

<br/>

## About this Project

In this Project we will analyze 3 species of Iris: *Iris Setosa, Iris Virginica* and *Iris Versicolor*.

The objects to be analyzed will be **SEPAL LENGTH**, **SEPAL WIDTH**, **PETAL LENGTH** and **PETAL WIDTH**, for this 3 species of Iris

***Image 4.***

![Iris Virginica](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/virginica.jpg)

<br/>

The script built to analyze the *iris dataset* is present in this repository and its name is *analysis.py*

The Iris Dataset file is available in [this repository](https://github.com/thenriq/Iris_dataset_Fisher) as well and its name is *[iris.data](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/iris.data)*.

Also, the raw data can be downloaded from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) and the Iris dataset collection is available [here](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data). 

After downloaded, both *iris.data* file and *analysis.py* file must be in the same folder

<br/>

## How to run the script *analysis.py*

After having followed steps from [*PRE-REQUISITES and INSTRUCTIONS*](#pre-requisites-and-instructions), the python interpreter can be issued from a command line on the terminal

To open the command-line interpreter:

•	On **Windows**, the command-line is called the *command prompt* or *MS-DOS* console. A quicker way to access it is to go to `Start menu → Run` and type `cmd.`

•	On **GNU/Linux** , the command-line can be accessed by several applications like *xterm, Gnome Terminal* or *Konsole*.

•	On **MAC OS X**, the system terminal is accessed through `Applications → Utilities → Terminal`.

Again, both *analysis.py* script and *iris.data* file must be in the same directory. Considering that the directory is going to be `c:\users\download\scripts`, once you are at the prompt, type as below:

***python analysis.py***

<br/>

### Script results and outputs

This script will create *4 histograms* in the origin folder, save a *text file* named *dataset.txt* with a summary of this dataset, print out on the terminal the *data amount* contained in the dataset, the *first 10 rows* in this datset, the *last 10 rows* and, in the end, it will *plot 10 diagrams* and *line plots* on screen. All tasks performed by this script will be described in detail below.

<br/>

### Analysing the results

All the libraries installed must be imported in order to enable it to run successfully. The commands used to import these libraries are described as below: *(lines 3-5)*

`import pandas as pd`

`import seaborn as sns`

`import matplotlib.pyplot as plt`


The code below was used to open the dataset: *(line 9)*

`filename = open("iris.data","r")`

Then, columns names were added with this code: *(line 10)*

`names = ['Sepal-Length', 'Sepal-Width', 'Petal-Length', 'Petal-Width', 'Species']`

An object named "*dataset*" was created using the code below from Pandas library in order to access and manipulate the *iris.data*'s file content: *(line 11)*

`dataset = pd.read_csv(filename,names=names)`

<br/>

The amont of data can be checked with the command below: *(line 15)*

`print(dataset.groupby('Species').size())`

***Table 1.***
Species         |TOTAL 
----------------|------
Iris-setosa    |	50
Iris-versicolor |	50
Iris-virginica  |	50

<br/>

Analysing the first 10 rows in the dataset: *(line 18)*

`print(dataset.head(10))`

***Table 2.***

Count|Sepal-Length|Sepal-Width|Petal-Length|Petal-Width|Species
-----|--------|-----------|------------|-----------|--------
0|5.1|3.5|1.4|0.2|Iris-setosa
1|4.9|3|1.4|0.2|Iris-setosa
2|4.7|3.2|1.3|0.2|Iris-setosa
3|4.6|3.1|1.5|0.2|Iris-setosa
4|5|3.6|1.4|0.2|Iris-setosa
5|5.4|3.9|1.7|0.4|Iris-setosa
6|4.6|3.4|1.4|0.3|Iris-setosa
7|5|3.4|1.5|0.2|Iris-setosa
8|4.4|2.9|1.4|0.2|Iris-setosa
9|4.9|3.1|1.5|0.1|Iris-setosa

<br/>

Analysing the last 10 rows in the dataset: *(line 21)*

`print(dataset.tail(10))`

***Table 3.***

Count|Sepal-Length|Sepal-Width|Petal-Length|Petal-Width|Species
---|---------|-----------|------------|-----------|---------
140|6.7|3.1|5.6|2.4|Iris-virginica
141|6.9|3.1|5.1|2.3|Iris-virginica
142|5.8|2.7|5.1|1.9|Iris-virginica
143|6.8|3.2|5.9|2.3|Iris-virginica
144|6.7|3.3|5.7|2.5|Iris-virginica
145|6.7|3|5.2|2.3|Iris-virginica
146|6.3|2.5|5|1.9|Iris-virginica
147|6.5|3|5.2|2|Iris-virginica
148|6.2|3.4|5.4|2.3|Iris-virginica
149|5.9|3|5.1|1.8|Iris-virginica

<br/>



A summary of the Iris dataset and its recording to the file *[dataset.txt](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/dataset.txt)* can be obtained by the command below: *(lines 25 - 26)*



`with open("dataset.txt","a") as f:`

`print((dataset.describe()),file = f)`

***Table 4***

Item|Sepal-length|Sepal-width|Petal-length|Petal-width
----|--------|-----------|------------|---------
count  |150|150|150|150
mean   |5.843333|3.054|3.758667|1.198667
std    |0.828066|0.433594|1.76442|0.763161
min    |4.3|2|1|0.1
25%|5.1|2.8|1.6|0.3
50%|5.8|3|4.35|1.3
75%|6.4|3.3|5.1|1.8
max    |7.9|4.4|6.9|2.5

From *Table 4* above, it is possible to  assume that the items in this dataset shows that the average size for the feature *petal* is smaller than the average size for the feature *sepal*. This can also be observed from the row *75%*. In other words, 75% of items from this dataset represents this difference between *sepal* and *petal*

<br/>

In this project, Histogram was used to analyse each feature individually in order to get an overall view and exported it to a png file using the commands below, from *Pyplot* library: *(lines 31 - 56)*

`dataset.hist(column='Sepal-Length',rwidth=0.9)
plt.title('Sepal Length')
plt.xlabel('Length (cm)')
plt.ylabel('Quantity')
plt.savefig('Sepal_Length.png')`

`dataset.hist(column='Sepal-Width',rwidth=0.9)
plt.title('Sepal Width')
plt.xlabel('Length (cm)')
plt.ylabel('Quantity')
plt.savefig('Sepal_Width.png')`

`dataset.hist(column='Petal-Length',rwidth=0.9)
plt.title('Petal Length')
plt.xlabel('Length (cm)')
plt.ylabel('Count')
plt.savefig('Petal_Length.png')`

`dataset.hist(column='Petal-Width',rwidth=0.9)
plt.title('Petal Width')
plt.xlabel('Length (cm)')
plt.ylabel('Count')
plt.savefig('Petal_Width.png')`

<br/>

***Histogram 1***

![Sepal Length](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/Sepal_Length.png)

<br/>

***Histogram 2***

![Sepal Width](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/Sepal_Width.png)

<br/>

***Histogram 3***

![Petal Length](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/Petal_Length.png)

<br/>

***Histogram 4***

![Petal Width](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/Petal_Width.png)

<br/>

<br/>

Also, a comparison of each variable on a different axis can be done with the code below, also from *Pyplot* library: *(line 87)*

`dataset.plot(figsize=(7, 10), subplots=True)`

***Line Chart 1.***

![Axes Compare](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/line_axes-compare.png)

We can observe on the chart above an increase on petal length and petal width, from  position 50 and then again from position 100. It indicates the size difference among these 3 species of iris: Iris setosa has the smallest petal (pos 1 to 50), and iris virginica, the largest (pos 100 to 150)

<br/>

We can also visualise and compare these data's attributes on a curve diagram using the function *FacetGrid* from *Seaborn*, on the code below: *(lines 113 - 123)*

`g = sns.FacetGrid(dataset,hue="Species",height=5)
g = g.map(sns.kdeplot, 'Sepal-Length').add_legend()`

`g = sns.FacetGrid(dataset,hue="Species",height=5)
g = g.map(sns.kdeplot, 'Sepal-Width').add_legend()`

`g = sns.FacetGrid(dataset,hue="Species",height=5)
g = g.map(sns.kdeplot, 'Petal-Length').add_legend()`

`g = sns.FacetGrid(dataset,hue="Species",height=5)
g = g.map(sns.kdeplot, 'Petal-Width').add_legend()`

<br/>

***Line Chart 2.***

![Sepal Length](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/line_sepal-length.png)

***Line Chart 3.***

![Sepal Width](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/line_sepal-width.png)

***Line Chart 4.***

![Petal Length](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/line_petal-length.png)

***Line Chart 5.***

![Petal Width](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/line_petal-width.png)

We can see again how these features differ in size and how Iris Versicolor and Iris Virginica are related to each other

<br/>

The data analysis can also be done with violin plot, from *Seaborn* library, using the code below. It shows the density of length and width in species. The thinner part represents the less dense data, while the fatter part represents more dense data. Data is being visualized by comparing all input variables (*petal* and *sepal* length and width) against the output variable, which is *species*: *(lines 92 - 100)*

`plt.figure(figsize=(9,7))
plt.subplot(2,2,1)
sns.violinplot(x="Species",y="Sepal-Length",data=dataset)`
`plt.subplot(2,2,2)
sns.violinplot(x="Species",y="Sepal-Width",data=dataset)`
`plt.subplot(2,2,3)
sns.violinplot(x="Species",y="Petal-Length",data=dataset)`
`plt.subplot(2,2,4)
sns.violinplot(x="Species",y="Petal-Width",data=dataset)`

<br/>

***Diagram 1.***

![Violin Plot](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/violin_plot.png)

<br/>

By comparing the species using scatter plot, also from *Seaborn* library, we can understand that the feature *sepal* is not sufficient to distinguish *Iris versicolor* from *Iris virginica*

On the other hand,  it is very clear how *Iris setosa* can be easily distinguished from *Iris versicolor* and *Iris virginica*

The scatterplot for *sepal* can be done using the command below: *(lines 77 - 78)*

`sns.scatterplot(x="Sepal-Length", y="Sepal-Width", data=dataset,  hue="Species")`
`plt.title("Sepal")`

<br/>

***Diagram 2.***

![Scatter Sepal](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/scatter_sepal.png)

The scatter plot for *petal* can be done using the command below: *(lines 82 - 83)*

`sns.scatterplot(x="Petal-Length", y="Petal-Width", data=dataset,  hue="Species")`
`plt.title("Petal")`

<br/>

***Diagram 3.***

![Scatter Petal](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/scatter_petal.png)

<br/>
<br/>

Another great way to visualize how these features are correlated to each other is using *heatmap*, also from *Seaborn* library, using the code below: *(lines 106 - 107)*

`plt.figure(figsize=(9,10))
sns.heatmap(dataset.corr(),annot=True)`

***Diagram 4.***

![Heat Map](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/Heat-map.png)

We can observe how *Petal Length* and *Petal Width* features are slightly correlated with *Sepal Length*, but not at all with *Sepal Width* 

<br/>
<br/>

Finally, let's visualize this dataset using the funcion boxplot, againf from *Seaborn: *(lines 64 - 72)*

`plt.figure(figsize=(12,10))`

`sns.boxplot(x="Species",y="Sepal-Length",data=dataset)
plt.subplot(2,2,2)`

`sns.boxplot(x="Species",y="Sepal-Width",data=dataset)
plt.subplot(2,2,3)`

`sns.boxplot(x="Species",y="Petal-Length",data=dataset)
plt.subplot(2,2,4)`

`sns.boxplot(x="Species",y="Petal-Width",data=dataset)`

***Diagram 5.***

![Box Plot](https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/plots/box_plot.png)

We can see how the category *species* is distrubuted with all other four input variables: *Sepals* and *Petals* length and width. While *Iris Setosa* and *Iris Virginica* differ high and low on each feature, *Iris Versicolor* keeps it in and average between *Iris Setosa* and *Iris Virginica* 

<br/>

# Final Notes

This dataset content is extremely interesting as it shows how it is possible to identify a certain object with high precision by only imputing a set of variables, and this variables having values so overlapping and close to each other that makes it impossible to guess the specie without analysing all the set of variables

More over and even more interesting is the fact that, after passed almost a century since this dataset was introduced, it is still in use nowadays and has been applied to the use and creation of artificial intelligence and machine learning, something so far away and futuristic from the time this dataset creators were alive. 

Iris dataset: small, but not trivial. Simple, but challenging. Real data.

<br/>

# REFERENCES

1.	https://archive.ics.uci.edu/ml/datasets/Iris
2.	https://en.wikipedia.org/wiki/Iris_flower_data_set
3.	R. A. Fisher (1936). "The use of multiple measurements in taxonomic problems". Annals of Eugenics. 7 (2): 179–188. doi:10.1111/j.1469-1809.1936.tb02137.x
4.	By Unknown author - https://www.adelaide.edu.au, Public Domain, https://commons.wikimedia.org/w/index.php?curid=42616717
5.	https://en.wikipedia.org/wiki/Fellow_of_the_Royal_Society
6.	https://matplotlib.org/
7.	Edgar Anderson (1935). "The irises of the Gaspé Peninsula". Bulletin of the American Iris Society. 59: 2–5.
8.	Edgar Anderson (1936). "The species problem in Iris". Annals of the Missouri Botanical Garden. 23 (3): 457–509. doi:10.2307/2394164. JSTOR 2394164
9.	http://www.nasonline.org/publications/biographical-memoirs/memoir-pdfs/anderson-edgar.pdf
10.	http://www.numpy.org/
11.	https://seaborn.pydata.org/
12.	https://pandas.pydata.org/

