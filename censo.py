import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


base_census = pd.read_csv('/home/thiago/Projects/machine-learning-course/adult/adult.data')
# print(base_census)
# print(base_census.describe()) # resumo
# print(base_census.isnull().sum()) # encontrar valores null

# print(np.unique(base_census['income'] , return_counts=True)) #  retorna valores unicos 

# grafico barras
# sns.countplot(x= base_census['income'])

# histograma
# plt.hist(x= base_census["age"])
# plt.hist(x= base_census["education-num"])
# plt.hist(x= base_census["hour-per-week"])
# plt.hist(x= base_census["hour-per-week"])
# plt.show()

# grafico = px.treemap(base_census, path=["workclass","age"])
# grafico = px.treemap(base_census, path=["occupation", "relationship"])
# grafico = px.treemap(base_census, path=["occupation", "relationship"])
# grafico = px.parallel_categories(base_census, dimensions=['occupation', "relationship"])
# grafico = px.parallel_categories(base_census, dimensions=["workclass","occupation", "relationship", "income"])
# grafico.show()