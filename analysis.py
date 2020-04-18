# Load libraries

import numpy as np
import seaborn as sns
import pandas as pd

from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn import datasets 
# Load Dataset

filename = open("iris.data","r")
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(filename,names=names)



# head
print(dataset.head(20))

# descriptions
with open("dataset.txt","a") as f:
    print((dataset.describe()),file = f)

# class distribution
print(dataset.groupby('class').size())


# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()



# histograms
# Sepal Length
dataset.hist(column='sepal-length',rwidth=0.9)
plt.title('Sepal Length')
plt.xlabel('Length (cm)')
plt.ylabel('Quantity')
plt.savefig('Sepal_Length.png')
#py.clf()

# Sepal Width
dataset.hist(column='sepal-width',rwidth=0.9)
plt.title('Sepal Width')
plt.xlabel('Length (cm)')
plt.ylabel('Quantity')
plt.savefig('Sepal_Width.png')
#py.clf()

# Petal Length
dataset.hist(column='petal-length',rwidth=0.9)
plt.title('Petal Length')
plt.xlabel('Length (cm)')
plt.ylabel('Quantity')
plt.savefig('Petal_Length.png')
#plt.clf()

# Petal Width
dataset.hist(column='petal-width',rwidth=0.9)
plt.title('Petal Width')
plt.xlabel('Length (cm)')
plt.ylabel('Quantity')
plt.savefig('Petal_Width.png')


plt.close("all") # closing all previous open plots


# Scatterplot
sns.scatterplot(x="sepal-length", y="sepal-width", data=dataset,  hue="class")
plt.title("Sepal")
plt.figure()


sns.scatterplot(x="petal-length", y="petal-width", data=dataset,  hue="class")
plt.title("Petal")
plt.show()

