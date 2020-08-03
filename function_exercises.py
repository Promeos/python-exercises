#!/usr/bin/env python
# coding: utf-8

# >After creating each function specified below, write the necessary code in order to test your function.
# 
# ## 1. 
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[3]:


def is_two(number):
    if number == '2':
        return True
    elif int(number) == 2:
        return True
    else:
        return False

print(is_two('2'))
print(is_two(2))
print(is_two(45))


# ## 2.
# > Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[22]:


def is_vowel(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if character.lower() in vowels and len(character) == 1:
        return True
    else:
        return False

print(('a is a vowel: {}').format(is_vowel('a')))
print(('A is a vowel: {}').format(is_vowel('A')))
print(('This sentence is a vowel: {}').format(
    is_vowel('This sentence is a vowel')
))
print(('G is a vowel: {}').format(is_vowel('G')))
print(('P is a vowel: {}').format(is_vowel('P')))


# ## 3.
# > Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[24]:


def is_consonant(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if character.lower() not in vowels and len(character) == 1:
        return True
    else:
        return False

print(('a is a consonant: {}').format(is_consonant('a')))
print(('A is a consonant: {}').format(is_consonant('A')))
print(('This sentence is a consonant: {}').format(
    is_consonant('This sentence contains may consonants')
))
print(('G is a consonant: {}').format(is_consonant('G')))
print(('P is a consonant: {}').format(is_consonant('P')))


# In[ ]:




