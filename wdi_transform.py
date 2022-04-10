#!/usr/bin/env python
# coding: utf-8

# In[142]:


url = 'https://raw.githubusercontent.com/lboltralik/world_data/main/WDI_Data.csv'
df = pd.read_csv(url)
pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[143]:


rcount = df.shape[0]
i=0
while i < rcount:
    df.iloc[i, 4:14] = df.iloc[i,4:14].fillna(df.iloc[i,4:14].mean())
    i += 1


# In[144]:


df["2020 [YR2020]"] = df["2020 [YR2020]"].fillna(df["2019 [YR2019]"])


# In[145]:


new_df = df.fillna(0)


# In[146]:


cwd = os.getcwd()
path = cwd + '/new_WDI_Data'
new_df.to_csv(path)


# In[ ]:




