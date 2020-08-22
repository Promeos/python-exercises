#!/usr/bin/env python
# coding: utf-8

# # 17 List Comprehension Problems in Python
# Creator: `Ryan Orsinger`
# 
# > Title: `list_comprehension_practice.py`
# 
# > Date: March 7th, 2019
# 
# > Source: https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a

# In[2]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# ## Exercise 1
# 
# > Rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

# In[3]:


uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)


# ## Exercise 2
# > Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
# 

# In[4]:


capitalized_fruits = [fruit.title() for fruit in fruits]
print(capitalized_fruits)


# ## Exercise 3
# > Exercise 3 - Use a list comprehension to make a variable named: fruits_with_more_than_two_vowels 
# Hint: You'll need a way to check if something is a vowel.

# In[5]:


fruits_with_more_than_two_vowels = [fruit for fruit in fruits if(
    (fruit.count('a')
    + fruit.count('e')
    + fruit.count('i')
    + fruit.count('o')
    + fruit.count('u'))
    > 2
    )]

print(fruits_with_more_than_two_vowels)


# ## Exercise 4 
# 
# > Make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# In[6]:


fruits_with_only_two_vowels = [fruit for fruit in fruits if(
    (fruit.count('a')
    + fruit.count('e')
    + fruit.count('i')
    + fruit.count('o')
    + fruit.count('u'))
    == 2
    )]

print(fruits_with_only_two_vowels)


# ## Exercise 5
# > Make a list that contains each fruit with more than 5 characters

# In[7]:


more_than_five_letters = [fruit for fruit in fruits if len(fruit) > 5]
print(more_than_five_letters)


# ## Exercise 6
# > make a list that contains each fruit with exactly 5 characters

# In[8]:


exactly_five_letters = [fruit for fruit in fruits if len(fruit) == 5]
print(exactly_five_letters)


# ## Exercise 7
# >Make a list that contains fruits that have less than 5 characters

# In[9]:


less_than_five_letters = [fruit for fruit in fruits if len(fruit) < 5]
print(less_than_five_letters)


# ## Exercise 8
# > Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# In[10]:


number_of_characters = [len(fruit) for fruit in fruits]
print(number_of_characters)


#  ## Exercise 9
#  >Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a".

# In[11]:


fruits_with_letter_a = [fruit for fruit in fruits if fruit.count('a')]
print(fruits_with_letter_a)


# In[12]:


# for fruit in fruits:
#     print(fruit.count('a'))


# ## Exercise 10
# > Make a variable named even_numbers that holds only the even numbers.

# In[13]:


even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


# ## Exercise 11
# > Make a variable named odd_numbers that holds only the odd numbers.

# In[14]:


odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)


# ## Exercise 12 
# > Make a variable named positive_numbers that holds only the positive numbers.

# In[15]:


positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)


# ## Exercise 13
# > Make a variable named negative_numbers that holds only the negative numbers

# In[16]:


negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)


# ## Exercise 14
# > Use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# In[17]:


more_than_two_numerals = [number for number in numbers if number <=-10 or number >= 10]
print(more_than_two_numerals)


# ## Exercise 15
# > Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# In[18]:


numbers_squared = [number * number for number in numbers]
print(numbers_squared)


# ## Exercise 16
# > Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# In[19]:


odd_negative = [number for number in numbers if number < 0 and number % 2 != 0]
print(odd_negative)


# ## Exercise 17
# > Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# In[20]:


numbers_plus_5 = [number + 5 for number in numbers]
print(numbers_plus_5)


# ## BONUS 
# > Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

# In[22]:


def prime_detector(value):
    is_prime = True
    
    # Prime numbers cannot be zero
    if value < 0:
        is_prime = False

    # 
    for i in range(2, value):
        if value % i == 0:
            is_prime = False

    if value == 1:
        return value
    elif is_prime:
        return value

# primes = [prime_detector(number) for number in numbers]
primes = [number for number in numbers if prime_detector(number) != None]
print(primes)

