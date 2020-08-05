#!/usr/bin/env python
# coding: utf-8

# >After creating each function specified below, write the necessary code in order to test your function.
# 
# ## 1. 
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[3]:


def is_two(number):
    if number == '2' or int(number) == 2:
        return True
    else:
        return False

print(is_two('2'))
print(is_two(2))
print(is_two(45))


# ## 2.
# > Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[4]:


def is_vowel(character):
    assert type(character) == str, "is_vowel function only takes a single character"
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if character.lower() in vowels and len(character) == 1:
        return True
    else:
        return False

#print(is_vowel(123))
print(('a is a vowel: {}').format(is_vowel('a')))
print(('A is a vowel: {}').format(is_vowel('A')))
print(('This sentence is a vowel: {}').format(
    is_vowel('This sentence is a vowel')
))
print(('G is a vowel: {}').format(is_vowel('G')))
print(('P is a vowel: {}').format(is_vowel('P')))


# ## 3.
# > Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[5]:


def is_consonant(character):
   
    if is_vowel(character) == False and len(character) == 1:
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
    
    if is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        return False

print(is_consonant_capitalize('house'))
print(is_consonant_capitalize('reddit'))


# ## 5.
# > Define a function named calculate_tip.
# - It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[7]:


def calculate_tip(tip_percentage, total_bill):
    return tip_percentage * total_bill

calculate_tip(.25, 100)


# ## 6.
# > Define a function named apply_discount.
# - It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[8]:


def apply_discount(original_price, discount_percentage):
    return original_price * (1-discount_percentage)

apply_discount(100, .25)


# ## 7.
# > Define a function named handle_commas. 
# - It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[9]:


def handle_commas(numeric_string):
    numeric_literal = int(numeric_string.replace(',',''))
    return numeric_literal

print(handle_commas('100,000,000'))
print(handle_commas('10,000,0000,000,0,0,0,0,00000')) # <- lol


# ## 8.
# > Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[10]:


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

# In[11]:


def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_with_removed_vowels = ''
    
    for letter in word:
        if is_consonant(letter) == True:
            word_with_removed_vowels += letter
    return word_with_removed_vowels

print(remove_vowels('House'))
print(remove_vowels('Big Cheese'))


# ## 10.
# > Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# 
# > - anything that is not a valid python identifier should be removed
# 
# >    - leading and trailing whitespace should be removed
# 
# >    - everything should be lowercase
# 
# >    - spaces should be replaced with underscores
# 
# for example:
# 
# -Name will become name
# 
# -First Name will become first_name
# 
# -% Completed will become completed
# 

# In[12]:


import keyword
keyword.kwlist

def normalize_name(word):
    
    word = word.lower().lstrip("\"'~`1234567890~!@#$%^&*()_+[]\|}{};'\"?><").replace(' ', '_')
    
    if word in keyword.kwlist:
        return "Come up with another variable name. That is a Python KEYWORD!"
    else:
        return word
    
print(normalize_name('11230984701982734Christopher 12345'))
print(normalize_name('and'))


# ## 11.
# > Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# 
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# 

# In[33]:


# This is a powerful and useful module. Incorporating accumulate function from
# itertools to perform cumulative addition on a sequence of numbers.
import itertools

# Each iteration of index, the sum function slices the
# the list of numbers up to BUT NOT INCLUDING the index above it!
# The sum function adds the numbers in the sliced list together!
# Place that iterative process in a list comprehension and bam, a sequential
# sum of cumulative values!
cumulative_sum = lambda sequence: list(itertools.accumulate(sequence))


# In[37]:


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_numbers2 = [2, 6, 8, 2, 56, 34, 7, 8]

print(cumulative_sum(list_of_numbers))
print(cumulative_sum(list_of_numbers2))


# # BONUS
# ## 1.
# > Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[17]:


def twelveto24(time_of_day):
    clock_24_hours = ''
    
    time_of_day = time_of_day.lower()
    
    if len(time_of_day) == 6:
        if 'am' in time_of_day:
            clock_24_hours = '0' + time_of_day.rstrip('am')
            return clock_24_hours
        elif 'pm' in time_of_day:
            clock_24_hours = str(int(time_of_day[0]) + 12) + time_of_day[1:].rstrip('pm')
            return clock_24_hours
        
    elif len(time_of_day) == 7:
        if 'am' in time_of_day:
            if int(time_of_day[:2]) == 12:
                clock_24_hours = "00" + time_of_day[2:].strip('am')
            else:
                clock_24_hours = time_of_day.rstrip('am')
                return clock_24_hours
        elif 'pm' in time_of_day:
            if int(time_of_day[:2]) == 12:
                clock_24_hours = time_of_day.rstrip('pm')
                return clock_24_hours
            else:
                clock_24_hours = str(int(time_of_day[:2]) + 12) + time_of_day[2:].rstrip('pm')
                return clock_24_hours


# In[18]:


print(twelveto24('3:00pm'))


# ## 2.
# > Create a function named col_index. It should accept a spreadsheet column name, and
# return the index number of the column.

# In[19]:


def col_index(column_name):
    column_group_value = 0
    last_column_value = 0
    total_column_value = 0
    
    letter_values = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
                     'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
                     'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,
                     'W':23,'X':24,'Y':25,'Z':26}
    
    if len(column_name) >= 2:
        for i in range(1, len(col_index)):
            for letter in column_name[:len(column_name)-1]: 
                column_group_value += (26**(len(column_name-i)) * letter_values[letter]
  
    for letter in letter_values:
        if letter == column_name[-1]:
            last_column_value += letter_values[letter]
    
    total_column_value = column_group_value + last_column_value
    return total_column_value    


# In[49]:


col_index('ZZA')


# In[ ]:


a = list(zip(itertools.count(1), ))


# In[ ]:




