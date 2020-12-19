#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
n=np.array([10,20,30,40])


# In[2]:


nn=np.array([[20,30,40,40],[22,33,44,55]])
nn


# In[4]:


n1=np.array([10,15,20,30])
np.intersect1d(n,n1)


# In[6]:


type(n1)


# In[8]:


nn=np.zeros((1,3))


# In[9]:


nn


# In[11]:


nn=np.zeros((2,4))
nn


# In[12]:


nn=np.zeros((5,5))
nn


# In[14]:


n1=np.full((2,2),10)
n1


# In[18]:


n1=np.full((2,4),12)
n1


# In[21]:


na=np.arange(1,10)
na


# In[23]:


na=np.arange(50,100,5)
na


# In[26]:


n1=np.random.randint (1,100,5)
n1


# In[30]:


n1=np.random.randint(1,10,5)
n1


# In[32]:


a1=np.array([[1,2,3,4],[4,5,6,7]])
a1.shape


# In[39]:


a1.shape=(2,4)
a1.shape


# In[40]:


a1


# In[42]:


a1.shape=(1,8)
a1


# In[45]:


a1.shape=(8,1)
a1


# In[55]:


a1=np.array([1,2,3,4,5])
a2=np.array([11,12,13,14,15])
np.vstack((a1,a2))


# In[56]:


a1=np.array([1,2,3,4,5,6])
a2=np.array([11,12,13,14,15,16])
np.hstack((a1,a2))


# In[60]:


np.column_stack((a1,a2))


# In[63]:


a=np.array([1,2,3,4])
b=np.array([1,4,5,0])
np.intersect1d(a,b)


# In[65]:


np.setdiff1d(a,b)


# In[66]:


np.setdiff1d(b,a)


# In[68]:


np.sum([a,b])


# In[70]:


np.sum([a,b],axis=0)


# In[71]:


np.sum([a,b],axis=1)


# In[73]:


a=a+1
a


# In[75]:


a=a-1
a


# In[77]:


a=a/1
a


# In[79]:


a=a*2
a


# In[81]:


a=np.array([1,2,3,4,5])
np.mean (a)


# In[83]:


a=np.array([1,2,4,5])
np.median(a)


# In[ ]:




