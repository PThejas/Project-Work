#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a program to find how many times substring “databricks” appears in the given string. (Try Atleast 2 methods) : 
#		Input : "databricks is unified Platform. databricks is based on spark"
#		Output : 2
s="databricks is unified Platform. databricks is based on spark"
print(s.count("databricks"))
    
s="databricks is unified Platform. databricks is based on spark"
data=s.split(" ")
cnt=0
for x in data:
        if x=='databricks':
            cnt=cnt+1
print(cnt)   


# In[ ]:




