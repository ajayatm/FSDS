#%%
import pandas as pd

# %%
df = pd.read_excel('Attribute DataSet.xlsx')
# %%
df
# %%
df.head()
# %%
pd.read_csv('haberman.csv', header=None)
# %%
pd.read_csv('haberman1.csv', header=None, sep='@',names=[1,2,3,4])
# %%
pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Smarket.csv')

# %%
a = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2015_totals.html')

# %%
type(a)
# %%
for i in a:
    print('-------------------------------------------------------')
    print(i)
    print('-------------------------------------------------------')
# %%
len(a)
# %%
pd.read_json('https://api.github.com/repos/pandas-dev/pandas/issues')
#%%
js = pd.read_json('https://api.github.com/repos/pandas-dev/pandas/issues')
# %%
js['user']
# %%
import os
os.cwd()
# %%
os.getcwd()
# %%
df
# %%
df.to_csv('test.csv')
# %%
df.to_csv('test1.csv',index=False)

