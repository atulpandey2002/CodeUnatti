#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = 1
print(a)


# In[2]:


pip install numpy


# In[3]:


pip install pandas


# In[4]:


pip install seaborn


# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns
#used for EDA


# In[3]:


import numpy as np


# In[4]:


#Scikit-Learn Lib
#Includes most of the classification, regression and clustering algos
import sklearn 


# pip install scikit-learn
# 

# In[5]:


pip install scikit-learn


# In[1]:


import sklearn


# In[2]:


from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[150,0]]))


# In[ ]:




