"""
1 .Find out there avarage rating on weekly basis keep this in a mind that they take two days of leave
2 .Total working days for each agents 
3. Total query that you hvae taken 
4. total Feedback that you have received 
5. a agent name who have average rating between 3.5 to 4 
6 . Agent name who have rating lesss then 3.5 
7 . agent name who have rating more then 4.5 
8 . how many feedaback agents have received more then 4.5 average
9 . average weekly response time for each agent 
10 . average weekely resolution time for each agents 
11 . list of all agents name 
12 . percentage of chat on which they have received a feedback 
13 . Total contributation hour for each and every agents weekly basis 
14. total percentage of active hour for a month 

sunny.savita@ineuron.ai ,sudhanshu@ineuron.ai
"""

# %%
import pandas as pd
# %%
df = pd.read_csv('AgentPerformance.csv')
# %%
df
# %%
df.dtypes
# %%
df['Dateformat'] = pd.to_datetime(df['Date'])
# %%
df.groupby(df['Agent Name'])['Average Rating'].mean()
# %%
df[df['Total Chats'] > 0]
# %%
df1 = df[df['Total Chats'] > 0]
# %%
df1
# %%
df1.groupby(df1['Datefomrat'].dt.week)['Average Rating'].mean()
# %%
df.groupby(df['Datefomrat'].dt.week)['Average Rating'].mean()
# %%
df1.groupby(df1['Dateformat'].dt.week)['Average Rating'].mean()
# %%
