#!/usr/bin/env python
# coding: utf-8

# ## 1. 
# > Import and test 3 of the functions from your functions exercise file.
# 

# In[6]:


import function_exercises


# > Import the module and refer to the function with the `.` syntax.

# In[7]:


function_exercises.is_two('2')


# > use `from` to import the function directly.

# In[8]:


from function_exercises import remove_vowels
remove_vowels('This is a sentence with vowels removed!')


# > Use `from` and give the function a different name.

# In[9]:


from function_exercises import twelveto24 as military_time
military_time("12:00pm")


# ## 1. 
# > How many different ways can you combine the letter from "abc" with the numbers 1, 2, 3?

# In[148]:


import itertools


# In[11]:


combinations_ABC123 = list(itertools.product('ABC', '123'))

print(f'The total number of combinations of ABC 1,2,3 is: {len(combinations_ABC123)}.')


# ## 2.
# > How many different ways can you combine two of the letters from "abcd"?

# In[12]:


combinations_of_2_abcd = list(itertools.combinations("abcd", 2))

print(f"The total number of 2 group combinations of 'abcd' is {len(combinations_of_2_abcd)}")


# In[337]:


# I import more_itertools and re modules to utilize the use of 'packaged' tools
# I don't know how they all work. Before I use a function I read its docstring to
# understand what the function does. If I need a visual aid, I'll look into the exocortex
# By testing, debugging, and incorporating them into my code I understand how they
# work a little bit more.
import json
import more_itertools
import re


# In[338]:


profiles_json = json.load(open('profiles.json'))

# Print out data type, key, and value information from profiles.json
print(type(profiles_json[0]))
print(profiles_json[0])


# > Total number of users

# In[222]:


# Learned something new: You cannot place an inline comment with a ? helper.
# Counts the entire length of an iterable.
get_ipython().run_line_magic('pinfo', 'more_itertools.ilen')
# Counts the number True's in an iterable. Return a single value of type int.
get_ipython().run_line_magic('pinfo', 'more_itertools.quantify')


# In[223]:


# I can use the ilen function from the more_itertools
# to find the length of an interable
total_profiles = more_itertools.ilen(profiles_json)
print(f"There are {total_profiles} users.")


# > Number of active users
# > Number of inactive users

# In[340]:


# I use a list comprehension and store of all values=[True\False] from key='isActive'.
is_active = [status['isActive'] for status in profiles_json]

# I use a list comprehension to store only False values using key='isActive'
# I stored active\inactive users differently so I could practice using
# the more_itertools module.
is_inactive = [status['isActive'] for status in profiles_json if(
    status['isActive'] != True)]

# These two functions are from the more_itertools module.
# more_itertools.quantify returns a single numeric value for all instances of bool->True
# The value returned is of type int
is_active_count = more_itertools.quantify(is_active)

# more_itertools.ilen returns the length of the iterator.
# `is_inactive` contains only False values. Like more_itertools.quantify
# more_itertools.ilen returns a single numeric value of type int
is_inactive_count = more_itertools.ilen(is_inactive)

print(f"Number of active users: {is_active_count}")
print(f"Number of inactive users {is_inactive_count}")


# > Grand total of all balance for all users

# In[339]:


# I use a list comprehension to 'pluck out' values from each user using key='balance'
# Once I get that value, I need to remove the $ and , characters using regex.
# After I remove those characters I can cast the value from str -> float.
# Once the iteration is complete I have a list properly formatted float values.
# I encapsulate the entire list comprehension inside a sum function. Summing all balances.
# The function returns a single value which I store in `grand_total`
grand_total = sum([float(
    re.sub(r"[$,]", '', account['balance'])) for account in profiles_json])

print(("Grand total balance for all users: ${:,}").format(grand_total))


# > Average balance per user

# In[341]:


# I divide `grand_total` by `total_profiles` and round by 2
# because were dealing with monetary values.
avg_balance_per_user = round(grand_total/total_profiles, 2)

print(("Average balance per user: ${:,}").format(avg_balance_per_user))


# > User with the lowest balance

# In[311]:


# Pack the user and user balance into a tuple.
# If packed each tuple as (name, balance) the min function would sort by name ascending
# Changing the order allows me to use the min function to find the lowest balance
# and person name with the lowest balance.
balance_and_name = [(person['balance'], person['name']) for person in profiles_json]

# Unpack the tuple after the min function selects the lowest balance from 
# `balance_and_name`.
lowest_balance, name_lowbal = min(balance_and_name)

print(f"User with the lowest balance: {name_lowbal} --- {lowest_balance}")


# In[310]:


# Utilizing the list of tuples, `balance_and_name` I can use the max function
# to find the maximum balance of all users. Because I grouped the balance
# and person name together, I need to unpack each tuple the same way I packed them.
highest_balance, name_highbal = max(balance_and_name)

print(f"User with the highest balance: {name_highbal} --- {highest_balance}")


# > Most common favorite fruit
# > Least common favorite fruit

# In[328]:


# I use a list comprehension to 'pluck out' all fruits using key=`favoriteFruit`.
favorite_fruits = [person['favoriteFruit'] for person in profiles_json]

# I use the set function to see unique `favoriteFruit` values in the dataset.
# print(set(favorite_fruits)) ---- 'banana', 'strawberry', 'apple'

# I used the count string method to count the instances of each fruit name.
total_bananas = favorite_fruits.count('banana')
total_strawberries = favorite_fruits.count('strawberry')
total_apples = favorite_fruits.count('apple')
# Display the value of each fruit counted
# print(total_bananas, total_strawberries, total_apples) banana-6, strawberry-9, apple-4

print(f"Most common favorite fruit: strawberry --- {total_strawberries}")
print(f"Least common favorite fruit: apple --- {total_apples}")


# > Total number of unread messages for all users

# In[336]:


# \D in regular expression notation finds all non digit character.
# 1)I use re.sub to find all non digits in greeting [str] and remove them, leaving numbers.
# 2)I pack the re.sub function inside an int function to cast the number from str -> int
# I place the function in a list comprehesion, where on each iteration it repeats 1 and 2
# After the iteration I pack the list comprehension in a sum function to calculate the
# total number of unread messages.
total_unread_messages = sum([int(
    re.sub("\D", '', person['greeting'])) for person in profiles_json])

print(f"Total number of unread messages for all users: {total_unread_messages}")

