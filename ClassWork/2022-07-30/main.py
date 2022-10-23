# %%
import pandas as pd
# %%
df = pd.read_csv('AgentLogingReport.csv')
# %%
df['Agent']
# %%
df[['Agent']]
# %%
type(df[['Agent']])
# %%
df.columns
# %%
df.describe()
# %%
df.dtypes
# %%
df.dtypes == 'object'
# %%
df.dtypes[df.dtypes == 'object'].index
# %%
df[df.dtypes[df.dtypes == 'object'].index]
# %%
df
# %%
df[df.dtypes[df.dtypes == 'object'].index].describe()
# %%
df['Agent'][:5:2]
# %%
df = pd.read_csv('AgentPerformance.csv')
# %%
df
# %%
df[df['Average Rating']==max(df['Average Rating'])]
# %%
df[df['Average Rating']==max(df['Average Rating'])]
# %%
df[df['Average Rating'] == 5.0]
# %%
df[df['Average Rating'] < 1.0]
# %%
pd.to_datetime(df['Date'])
# %%
df['DateDate'] = pd.to_datetime(df['Date'])
# %%
df
# %%
df.dtypes
# %%
max(df['DateDate'])
# %%
min(df['DateDate'].dt.isocalendar().week)
# %%
df['DateDate'].dt.isocalendar().week
# %%
df['DateDate'].dt.isocalendar()
# %%
df[df['DateDate'].dt.day == 30]
# %%
df[df['Average Rating'] == 5.0]
# %%
df[df['Average Rating'] == 5.0]['DateDate'].dt.day
# %%
df
# %%
df['DateDate'].dt.day.value_counts()
# %%
df[df['Average Rating'] == 5.0]['DateDate'].dt.day.value_counts()
# %%
df['Date'][:5]
# %%
df.iloc[300:700,3:8]
# %%
df
# %%
df.groupby(df['DateDate'].dt.day)['Average Rating'].mean()
# %%
df
# %%
df.dtypes
# %%
