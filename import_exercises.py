#!/usr/bin/env python
# coding: utf-8

# ## 1. 
# > Import and test 3 of the functions from your functions exercise file.
# 

# In[2]:


import function_exercises


# > Import the module and refer to the function with the `.` syntax.

# In[3]:


function_exercises.is_two('2')


# > use `from` to import the function directly.

# In[4]:


from function_exercises import remove_vowels
remove_vowels('This is a sentence with vowels removed!')


# > Use `from` and give the function a different name.

# In[5]:


from function_exercises import twelveto24 as military_time
military_time("12:00pm")


# ## 1. 
# > How many different ways can you combine the letter from "abc" with the numbers 1, 2, 3?

# In[6]:


import itertools


# In[7]:


combinations_ABC123 = list(itertools.product('ABC', '123'))

print(f'The total number of combinations of ABC 1,2,3 is: {len(combinations_ABC123)}.')


# ## 2.
# > How many different ways can you combine two of the letters from "abcd"?

# In[8]:


combinations_of_2_abcd = list(itertools.combinations("abcd", 2))

print(f"The total number of 2 group combinations of 'abcd' is {len(combinations_of_2_abcd)}")


# In[9]:


import json


# In[42]:


profiles_json = json.load(open('profiles.json'))
profiles_data_formatted = json.dumps(profiles_json, indent=1)


# In[43]:


print(profiles_data_formatted)


# In[82]:


def profile(data):
    return data[0]

total_number_of_users = list(itertools.groupby(profiles_data_formatted, profile))


# In[85]:


total_number_of_users = list(itertools.ifilter('_id', profiles_data_formatted))


# In[53]:





# In[79]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




