# %%
import numpy as np
#%%
l1 = [1,2,3,4,5]
ar1 = np.array(l1)
# %%
ar1
# %%
l2 = [1,2,3,4,5,3.4]
ar2 = np.array(l2)
# %%
l3 = [1,2,3,4,5,3.4,'a']
ar3 = np.array(l3)
# %%
l2
# %%
l3
# %%
ar1.ndim
# %%
ar4 = np.array([[[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]],[[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]])
# %%
ar4.ndim
# %%
ar3.size
# %%
ar4.size
# %%
ar4.shape
# %%
ar3.shape
# %%
np.random.randint(0,100, (2,3,4))
# %%
np.random.randn(3,3)
# %%
type(ar3[1])
# %%
ar3[::-1]
# %%
ar2
# %%
ar3
# %%
a6 = np.random.randint(0,101,(5,5))
# %%
a6>50
# %%
a6[a6>50]
# %%
a7 = np.random.randint(0,10,(2,2))
a8 = np.random.randint(0,10,(2,2))
# %%
a7*a8
# %%
a7
# %%
a8
# %%
a7@a8
# %%
a7*2
# %%
a7/0
# %%
np.sqrt(a7*a8)
# %%
np.sqrt(a7@a8)
# %%
np.arange(0,10,1.5)
# %%
np.linspace(2,3,num=101)
# %%
np.linspace(0,101,num=101,retstep=True)
# %%
np.logspace(2,4,num=4,base=10)
# %%
np.eye(10)
# %%
