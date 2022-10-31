# %%
import cufflinks as cf
import numpy as np
import pandas as pd
import seaborn as sns

# %%
a = pd.DataFrame(np.random.randint(1,100, (100,1)))
# %%
a.iplot()
# %%
cf.go_offline()
# %%
a
# %%
b = pd.DataFrame(np.random.randint(1,100, (20,10)), columns=[1,2,3,4,5,6,7,8,9,10])
# %%
b.iplot()
# %%
b.iplot(x=1,y=2,mode='markers')
# %%
c = sns.load_dataset('titanic')
# %%
c.iplot(x='age',y='fare',mode='markers')
# %%
c.iplot(x='pclass',y='fare',mode='markers')
# %%
c.iplot(kind = 'bar', x='pclass',y='survived')
# %%
c.plot(kind = 'bar', x='pclass',y='survived')
# %%
