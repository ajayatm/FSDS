# %%
from cProfile import label
import pandas as pd
import numpy as np
import seaborn as sns
import cufflinks as cf
import matplotlib.pyplot as plt
import plotly.io as pio

# %%
a = sns.load_dataset('iris')
# %%
a.iplot()
# %%
cf.go_offline()
# %%
a.plot()
# %%
a.plot(x='species')
# %%
a.plot.scatter(x='sepal_length', y='petal_length')
# %%
a.plot.scatter(x='sepal_length', y='petal_length',c='sepal_width')
# %%
a.plot.scatter(x='sepal_length', y='petal_length',c='sepal_width', s = 10)
# %%
a.plot.hexbin(x='sepal_length', y='petal_length',gridsize=10)
# %%
from mpl_toolkits import mplot3d
# %%
x = np.linspace(-1,6,30)
# %%
y = np.linspace(-1,6,30)
# %%
z = (x+y)/2
# %%
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot3D(x,y,z)
# %%
a.iloc[5:11].plot(kind='barh',figsize=(20,10))
# %%
a['petal_length'].plot(kind='hist',figsize=(20,10))
# %%
a.hist(figsize=(20,10))
# %%
cf.go_offline()
# %%
a.iplot()
# %%
a.iplot(x='sepal_length',y='sepal_width', size='petal_width',kind='bubble')
# %%
a
# %%
a.iplot(x='sepal_length',y='sepal_width',z='petal_length',size='petal_width',kind='bubble3d')
# %%
b = sns.load_dataset('tips')
# %%
b
# %%
b.plot(x='total_bill',y='tip',kind='scatter')
# %%
b.iplot(x='total_bill',y='tip',mode='markers')
# %%
sns.relplot(x='total_bill',y='tip',data=b)
# %%
b['smoker'].value_counts()
# %%
sns.relplot(x='total_bill',y='tip',data=b,style='smoker',hue='sex',col='time')
# %%
sns.relplot(x='total_bill',y='tip',data=b,style='smoker',hue='sex',col='time',size='size')
# %%
a
# %%
b
# %%
b.iplot()
# %%
pio.renderers
# %%
pio.renderers.default = "vscode"
# %%
