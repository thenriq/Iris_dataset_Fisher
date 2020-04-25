# Iris_dataset_Fisher
Project 2020 Programing and Scripting GMIT
<br/><br/>

# INTRODUCTION
## What is the Iris Flower Dataset 

The IRIS FLOWER DATA SET is a classic data set introduced by Ronald Fisher in 1930[1]. It is used in statistics methods and machine learning and consists of four continuous characters for three species of Iris: IRIS SETOSA, IRIS VERSICOLOR and IRIS VIRGINICA. This characters are SEPAL LENGTH, SEPAL WIDTH, PETAL LENGTH and PETAL WIDTH. It contains 150 objects of three different classes, with 50 numeric set values in cm for each class, which one is linearly separable from the other classes, while the other classes are not linearly separable from each other. This data set is available for download from UC Irvine Machine Learning Repository
<br/>
The species in the Iris flower dataset are distributed on the range below:
From position 1 to position : IRIS SETOSA
from position  51 to position100: IRIS VERSICOLOR
from position 101 to position 150: IRIS VIRGINICA

# RESEARCH
This dataset was introduced by the British statistician and biologist **Ronald Fisher** in his 1936 paper *"The use of multiple mesurements in Taxonomic problems  as an example of linear discriminant analysis"* [8 and 9]

## Who was Ronald Fisher

![Ronald Fisher] (https://github.com/thenriq/Iris_dataset_Fisher/blob/master/images/Youngfisher.JPG)

<p align="left">
   Sir Ronald Aylmer Fisher, British statistician and geneticist (February 17, 1980 - July 29, 1962) - image from 6
</p>
<br/>
Sir Ronald Aylmer Fisher was one of the most brilliant scientists from the 20th century, considered the greatest biologist since Charles Darwin. His lifework with genetic and statistics made him be described as "a genius who almost single-handedly created the foundations for modern statistical science" and "the single most important figure in 20th century statistics".
He was also awarded as a **Fellow of the Royal Society (FRM)** [7] and made a **Knight Bachelor** by *Queen Elizabeth II* in 1952. In 1958, we was awarded with the **Linnean Society of London Darwin-Wallace Medal**

<br/><br/>
## Why was this data collected

<br/>

This information were collected by **Edgar Anderson** for his publication in 1936  as it seemed to be an ideal study case about genetic variation and test hypotheses of intra  morphological variation. Iris versicolor seems to be a mix between Iris virginica and iris setosa, which might indicate a case of hybridisation between these two species[8]
<br/>
<p align="center">
   <img src="images/irises.png" width=601 height=268>
</p>
<p align="center">
Irises - Image from 4
</p>

<br/><br/>

## Collection method

<br/>

*Iris setosa* and *Iris versicolor* data were collected in the Gaspé Peninsula *"all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"*  and then published by **Edgar** in *1935*. The same method was certainly applied for *Iris virginica* before Edgar shared this data with the British statistician and biologist Ronald Aylmer Fisher in 1937 
<br/>
<br/>
<p align="center">
   <img src="images/Edgar_Anderson.jpg" width=166 height=224>
</p>
<p align="center">
Edgar Shannon Anderson, american botanist  (November 9, 1897 – June 18, 1969). Figure from 5
</p>

<br/><br/>

# DATASET ANALYSIS
## PRE-REQUISITES and INSTRUCTIONS
<br/>
Requirements to successfully run the scripts on this project is to have the Python interpreter installed on a computer. Steps on how to download and install Python can be obtained from the link https://www.python.org/downloads
<br/>
Also, a number of libraries must be installed and imported before running this script. The install process can be done from the Command prompt (cmd). 

Steps to install libraries:

SEABORN: pip install seaborn

PANDAS: pip install pandas

MATPLOTLIB: pip install matplotlib

<br/>

**SEABORN** - Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

**PANDAS** - pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.

**MATPLOTLIB** - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
<br/>

Steps to import libraries:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

<br/>

## PLOTS AND TABLES

In this Project we will analyze 3 species of Iris: *Iris Setosa, Iris Virginica* and *Iris Versicolor*.
The objects to be analyzed will be **SEPAL LENGTH**, **SEPAL WIDTH**, **PETAL LENGTH** and **PETAL WIDTH**, for this 3 species of Iris

The amont of data can be checked with the command below:

`print(dataset.groupby('Species').size())`

***TABLE 1.***
Species         |TOTAL 
----------------|------
Iris-setosa    |	50
Iris-versicolor |	50
Iris-virginica  |	50

<br/>

***TABLE 2.***

Analysing the first 10 rows in the dataset:

`print(dataset.head(10))`

|Sepal-Length|Sepal-Width|Petal-Length|Petal-Width|Species
-------------|-----------|------------|-----------|--------
1|5.1|3.5|1.4|0.2|Iris-setosa
2|4.9|3|1.4|0.2|Iris-setosa
3|4.7|3.2|1.3|0.2|Iris-setosa
4|4.6|3.1|1.5|0.2|Iris-setosa
5|5|3.6|1.4|0.2|Iris-setosa
6|5.4|3.9|1.7|0.4|Iris-setosa
7|4.6|3.4|1.4|0.3|Iris-setosa
8|5|3.4|1.5|0.2|Iris-setosa
9|4.4|2.9|1.4|0.2|Iris-setosa
10|4.9|3.1|1.5|0.1|Iris-setosa

<br/>

***TABLE 3.***

Analysing the last 10 rows in the dataset:

`print(dataset.tail(10))`

Sepal-Length|Sepal-Width|Petal-Length|Petal-Width|Species
------------|-----------|------------|-----------|---------
142|6.9|3.1|5.1|2.3|Iris-virginica
143|5.8|2.7|5.1|1.9|Iris-virginica
144|6.8|3.2|5.9|2.3|Iris-virginica
145|6.7|3.3|5.7|2.5|Iris-virginica
146|6.7|3|5.2|2.3|Iris-virginica
147|6.3|2.5|5|1.9|Iris-virginica
148|6.5|3|5.2|2|Iris-virginica
149|6.2|3.4|5.4|2.3|Iris-virginica
150|5.9|3|5.1|1.8|Iris-virginica

<br/>

***TABLE 4***

A summary of the Iris dataset can be obtained by the command below:

`print(dataset.describe())`
sepal-length|sepal-width|petal-length|petal-width
------------|-----------|------------|---------
count  |150|150|150|150
mean   |5.843333|3.054|3.758667|1.198667
std    |0.828066|0.433594|1.76442|0.763161
min    |4.3|2|1|0.1
25%|5.1|2.8|1.6|0.3
50%|5.8|3|4.35|1.3
75%|6.4|3.3|5.1|1.8
max    |7.9|4.4|6.9|2.5




## REFERENCES
1. https://en.wikipedia.org/wiki/Ronald_Fisher
2. https://www.marylandbiodiversity.com/viewSpecies.php?species=357
3. https://towardsdatascience.com/neural-network-on-iris-data-4e99601a42c8
4. https://www.pluralsight.com/guides/designing-a-machine-learning-model
5. http://www.nasonline.org/publications/biographical-memoirs/memoir-pdfs/anderson-edgar.pdf
6. By Unknown author - https://www.adelaide.edu.au, Public Domain, https://commons.wikimedia.org/w/index.php?curid=42616717
7. https://en.wikipedia.org/wiki/Fellow_of_the_Royal_Society
8. https://en.wikipedia.org/wiki/Iris_flower_data_set
9. R. A. Fisher (1936). "The use of multiple measurements in taxonomic problems". Annals of Eugenics. 7 (2): 179–188. doi:10.1111/j.1469-1809.1936.tb02137.x
