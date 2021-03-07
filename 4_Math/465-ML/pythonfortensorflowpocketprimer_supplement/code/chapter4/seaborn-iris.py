# https://github.com/mwaskom/seaborn-data 
import seaborn as sns
import matplotlib.pyplot as plt

# load iris data
iris = sns.load_dataset("iris")

# construct iris plot
sns.swarmplot(x="species", y="petal_length", data=iris)

# show plot
plt.show()

