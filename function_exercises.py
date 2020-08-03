#!/usr/bin/env python
# coding: utf-8

# >After creating each function specified below, write the necessary code in order to test your function.
# 
# ## 1. 
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[1]:


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

# In[2]:


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

# In[3]:


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


# ## 4. 
# > Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[6]:


def is_consonant_capitalize(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if word[0] not in vowels:
        word = word.capitalize()
        return word
    else:
        return False

print(is_consonant_capitalize('house'))
print(is_consonant_capitalize('reddit'))


# ## 5.
# > Define a function named calculate_tip.
# - It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[8]:


def calculate_tip(tip_percentage, total_bill):
    return tip_percentage * total_bill

calculate_tip(.25, 100)


# ## 6.
# > Define a function named apply_discount.
# - It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[10]:


def apply_discount(original_price, discount_percentage):
    return original_price * (1-discount_percentage)

apply_discount(100, .25)


# ## 7.
# > Define a function named handle_commas. 
# - It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[15]:


def handle_commas(numeric_string):
    numeric_literal = int(numeric_string.replace(',',''))
    return numeric_literal

print(handle_commas('100,000,000'))
print(handle_commas('10,000,0000,000,0,0,0,0,00000')) # <- lol


# ## 8.
# > Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[21]:


def get_letter_grade(grade):
        if grade >= 89:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        elif grade >= 0:
            return 'F'
        else:
            return None

print(get_letter_grade(100))
print(get_letter_grade(59.99999999999999999999)) # It actually rounds up to a D!?!
print(get_letter_grade(-100))


# ## 9.
# > Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[ ]:


def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    word.replace()


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




