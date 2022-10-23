# %%
import pandas as pd
df = pd.read_csv('AgentPerformance.csv')
df['Dateformat'] = pd.to_datetime(df['Date'])
df1 = df[df['Total Chats'] > 0]
# %%
#1 .Find out there avarage rating on weekly basis keep this in a mind that they take two days of leave
df1.groupby(['Agent Name',df1['Dateformat'].dt.isocalendar().week])['Average Rating'].mean()
# %%
#2 .Total working days for each agents
df1.groupby('Agent Name')['Date'].size()
#%%
#3. Total query that you hvae taken 
df1.groupby('Agent Name')['Total Chats'].size()
# %%
#4. total Feedback that you have received
df1.groupby('Agent Name')['Total Feedback'].sum()
# %%
#5. a agent name who have average rating between 3.5 to 4
df2 = df1.groupby('Agent Name')['Average Rating'].mean().between(3.5,4).to_frame()
df2[df2['Average Rating'] == True]
# %%
# %%
#6 . Agent name who have rating lesss then 3.5
df1[df1['Average Rating'] < 3.5]['Agent Name'].unique()
# %%
#7 . agent name who have rating more then 4.5
df1[df1['Average Rating'] > 4.5]['Agent Name'].unique()
# %%
#8 . how many feedaback agents have received more then 4.5 average
df3 = df1.groupby('Agent Name')['Average Rating'].mean().to_frame()
df3[df3['Average Rating'] > 4.5]
# %%
#9 . average weekly response time for each agent
df1['Mean Resp Time'] = pd.to_datetime(df1['Average Response Time'])
df1.groupby('Agent Name')['Mean Resp Time'].mean()
# %%
#10 . average weekely resolution time for each agents
df1['Mean Resol Time'] = pd.to_datetime(df1['Average Resolution Time'])
df1.groupby('Agent Name')['Mean Resol Time'].mean()
# %%
#11 . list of all agents name 
list(df['Agent Name'].unique())
# %%
#12 . percentage of chat on which they have received a feedback
df4 = df1.groupby('Agent Name')['Total Chats','Total Feedback'].sum()
df4['Feedback Percentage'] = df4['Total Feedback']/df4['Total Chats']*100
df4[['Feedback Percentage']]
# %%
#13. Total contributation hour for each and every agents weekly basis 
# %%
df01 = pd.read_csv('AgentLogingReport.csv')
# %%
df01['week'] = pd.to_datetime(df01['Date']).dt.isocalendar().week
# %%
df01['Duration Hour'] = pd.to_datetime(df01['Duration']).dt.hour
# %%
df01['Duration Minute'] = pd.to_datetime(df01['Duration']).dt.minute
# %%
df01['Duration Second'] = pd.to_datetime(df01['Duration']).dt.second
# %%
df01['Duration in Hours'] = df01['Duration Hour'] + df01['Duration Minute']/60 + df01['Duration Second']/3600
# %%
df01.groupby(['Agent','week'])['Duration in Hours'].sum()
# %%
#14. total percentage of active hour for a month 
#Assuming 21 working days in July 2022 and 8 hours shift per day
df01.groupby('Agent')['Duration in Hours'].sum()/8/21*100
# %%
