#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv("Height")


# In[6]:


df


# In[ ]:


df.rename(columns= {"Mention your height (in cm)": "Height",}, inplace= True)


# In[13]:


df


# In[15]:


df["height"].value_counts()


# In[14]:


str.upper(df.iloc[32,1])


# In[16]:


df.tail(12)


# In[17]:


df.tail()


# In[20]:


df['height']*2


# In[21]:


df


# In[22]:


df.iloc[2:6,[1]]


# In[26]:


list = [str.isdigit(ele) for ele in df.height]
list


# In[27]:





# In[28]:


df.height[list]


# In[32]:


lii = [ele for ele in df['height'].str.upper() if 'CM' in ele]
lii


# In[30]:


df['height']


# In[33]:


req_li= [ele.split()[0] for ele in lii]
req_li


# In[36]:


df= pd.DataFrame(df['height'].str.upper().replace(lii,req_li), columns=['height'])
df


# In[45]:


df.iloc[3,0] = 165
df.iloc[21,0] = 0


# In[46]:


df1= df.drop(labels= 21, axis=0)
df1


# In[48]:


df= df.astype({'height':float})
df1= df1.astype({'height':float})
df1


# In[4]:


df.iloc[21,0]= np.mean(df1.height)


# In[52]:


df


# In[2]:


get_ipython().system('pip install numpy')


# In[ ]:




