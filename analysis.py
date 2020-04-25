# Load libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load Dataset
filename = open("iris.data","r") # Opening and reading file iris.data
names = ['Sepal-Length', 'Sepal-Width', 'Petal-Length', 'Petal-Width', 'Species'] # Added columns names to dataset
dataset = pd.read_csv(filename,names=names) # Creating dataset with filename and names above


# Species distribution
print(dataset.groupby('Species').size()) # prints a total of each specie in dataset

# head
print(dataset.head(10)) # Prints the first 10 rows in dataset

#tail
print(dataset.tail(10)) # Prints the last 10 rows in dataset


# descriptions
with open("dataset.txt","a") as f: #creating file dataset.txt in append mode
    print((dataset.describe()),file = f) #outputing dataset summary to dataset.txt file


# histograms (pyplot)
# Sepal Length
dataset.hist(column='Sepal-Length',rwidth=0.9)
plt.title('Sepal Length')
plt.xlabel('Length (cm)')
plt.ylabel('Count')
plt.savefig('Sepal_Length.png')

# Sepal Width
dataset.hist(column='Sepal-Width',rwidth=0.9)
plt.title('Sepal Width')
plt.xlabel('Length (cm)')
plt.ylabel('Count')
plt.savefig('Sepal_Width.png')

# Petal Length
dataset.hist(column='Petal-Length',rwidth=0.9)
plt.title('Petal Length')
plt.xlabel('Length (cm)')
plt.ylabel('Count')
plt.savefig('Petal_Length.png')

# Petal Width
dataset.hist(column='Petal-Width',rwidth=0.9)
plt.title('Petal Width')
plt.xlabel('Length (cm)')
plt.ylabel('Count')
plt.savefig('Petal_Width.png')

plt.close("all") # closing all previous open plots. 
                 # If not closed here, they will show up from below, when outputing next plots


# box plot (pyplot)
# Using box plot to see how the category SPECIES is distrubuted with all other four input variables: Sepals and Petals length and width
plt.figure(figsize=(12,10)) # Setting a window size for this plot
plt.subplot(2,2,1)
sns.boxplot(x="Species",y="Sepal-Length",data=dataset)
plt.subplot(2,2,2)
sns.boxplot(x="Species",y="Sepal-Width",data=dataset)
plt.subplot(2,2,3)
sns.boxplot(x="Species",y="Petal-Length",data=dataset)
plt.subplot(2,2,4)
sns.boxplot(x="Species",y="Petal-Width",data=dataset)


# Scatterplot SEPAL (seaborn)
plt.figure()
sns.scatterplot(x="Sepal-Length", y="Sepal-Width", data=dataset,  hue="Species")
plt.title("Sepal")

# Scatterplot PETAL (seaborn)
plt.figure()
sns.scatterplot(x="Petal-Length", y="Petal-Width", data=dataset,  hue="Species")
plt.title("Petal")


#LinePlot (pyplot)
dataset.plot(figsize=(7, 10), subplots=True)


# Violin Plot (pyplot)
# Using Violin plot to show the density of length and width in species. Thinner part: less dense; bigger part: more dense
plt.figure(figsize=(9,7))
plt.subplot(2,2,1)
sns.violinplot(x="Species",y="Sepal-Length",data=dataset)
plt.subplot(2,2,2)
sns.violinplot(x="Species",y="Sepal-Width",data=dataset)
plt.subplot(2,2,3)
sns.violinplot(x="Species",y="Petal-Length",data=dataset)
plt.subplot(2,2,4)
sns.violinplot(x="Species",y="Petal-Width",data=dataset)


# Heat map (seaborn)
# Using a Heatmap to show how these 4 features are correlated to each other
# Sepal Length and Sepal Width are slightly correlated to each other
plt.figure(figsize=(9,10))
sns.heatmap(dataset.corr(),annot=True)


# faceting (seaborn)
# Using Faceting plot to compare the four input features with species
# This plotting show that the  feature "SEPAL" is not sufficient to distinguish Iris versicolor from Iris virginica 
g = sns.FacetGrid(dataset,hue="Species",height=5)
g = g.map(sns.kdeplot, 'Sepal-Length').add_legend()

g = sns.FacetGrid(dataset,hue="Species",height=5)
g = g.map(sns.kdeplot, 'Sepal-Width').add_legend()

g = sns.FacetGrid(dataset,hue="Species",height=5)
g = g.map(sns.kdeplot, 'Petal-Length').add_legend()

g = sns.FacetGrid(dataset,hue="Species",height=5)
g = g.map(sns.kdeplot, 'Petal-Width').add_legend()



# Outputing all plots created above (all but histograms)
plt.show()




