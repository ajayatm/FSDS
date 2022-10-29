# %%
import pandas as pd
# %%
data = {'name':['ajay','michelle','sagini','emil'],
        'salary':[100,200,300,400],
        'addr':['blr','tor','nyc','tor']
        }

# %%
pd.DataFrame(data)
# %%
df = pd.DataFrame(data)
# %%
df.loc[3:6]
# %%
df.iloc[1:4]
# %%
data1 = {
    'pf':[1,2,3,4],
    'tax':[5,6,7,8],
    'course':[3,4,5,6]
}
# %%
df1 = pd.DataFrame(data1)
# %%
pd.concat([df,df1], axis=0)
# %%
df
# %%
df1
# %%
data2 = {'empid':[1,2,3,4],'salary':[100,200,300,400],'pf':[5,6,7,8]}
data3 = {'empid':[1,2,3,4],'addr':['tor','nyc','del','bos'],'mob':[351351,313131,354654,321434]}
# %%
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
# %%
df2
df3
# %%
df3
# %%
df2
# %%
pd.merge(df2,df3)
# %%
pd.merge(df2,df3, how='left')
# %%
pd.merge(df2,df3,how='right',on='empid')
# %%
data3 = {'empid3':[1,2,3,4],'salary':[100,200,300,400],'pf':[5,6,7,8]}
data4 = {'empid4':[1,2,3,4],'addr':['tor','nyc','del','bos'],'mob':[351351,313131,354654,321434]}
# %%
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)
# %%
df3
# %%
df4
# %%
pd.merge(df3,df4,left_on='empid3',right_on='empid4',how='inner')
# %%
df_sales = pd.read_csv('sales_data_final.csv')
# %%
df_sales
# %%
df_sales.head()
# %%
def profit_flag(a):
    if a >= 0:
        return 'Positive'
    else:
        return 'Negative'
# %%
df_sales['profit_flag'] = df_sales['profit'].apply(profit_flag)
# %%
def quantity_flag(a):
    if a < 10:
        return 'Low'
    elif a > 10 and a < 20:
        return 'Medium'
    else:
        return 'High'

# %%
df_sales['quantity_flag'] = df_sales['quantity'].apply(quantity_flag)
# %%
df_sales['quantity^2'] = df_sales['quantity'].apply(lambda a:a**2)
# %%
