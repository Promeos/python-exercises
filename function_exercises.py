#!/usr/bin/env python
# coding: utf-8

# >After creating each function specified below, write the necessary code in order to test your function.
# 
# ## 1. 
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[161]:

def is_two(number):
    # This function a number. If the number is either the numeric literal 2, or the string literal 2
    # return True
    if number == '2' or int(number) == 2:
        return True
    # Else the funciton will return False
    else:
        return False

print(is_two('2'))
print(is_two(2))
print(is_two(45))


# ## 2.
# > Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[18]:


def is_vowel(character):
    assert type(character) == str, "is_vowel function only takes a single character"
    # Create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Because the is_vowel function accepts a single character, I can use the
    # 'in' keyword to test whether 'character' is a 'member'/ is in the list of
    # vowels. In order to make this evaluation and comparison, I used the string method .lower().
    # This string method will convert any uppercase character to lowercase. This allows me to 
    # properly test membership of 'character' in list vowels. Compare apples to apples so to speak.
    # The len()... conditional expression added to ensure a string literal of length 1. 
    # 
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

# In[22]:


def is_consonant(character):
   # I had to look up what a consonant is. I realized I could use my handy dandy is_vowel function,
   # which I labored over a hot computer for. The is_vowel function only returns True if 'character'
   # is a vowel! I can use the output from is_vowel to evaluate the first part of the compound conditional
   # expression as True. False == False <---- True, Am I right? If is_vowel is False, then 'character' is a
   # consonant. Similar to the if clause in the is_vowel function, I added a len() function to ensure
   # the string literal passed has a length of 1 character.

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

# In[23]:


def is_consonant_capitalize(word):
    # Now, I've been building these functions and placing functions inside of functions - Functionception.
    # Let's add one more layer. I use the is_consonant function to determine whether a sting is a consonant
    # INSIDE of the consonant function I use string indexing to access the first character of the word parameter.
    # If the first character of the string literal passed is a consonant, then I want to capitalize it.
    # Otherwise I'll return False.

    if is_consonant(word[0]) == True:
        return word.capitalize()
    else:
        return False

print(is_consonant_capitalize('house'))
print(is_consonant_capitalize('reddit'))


# ## 5.
# > Define a function named calculate_tip.
# - It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[8]:


def calculate_tip(tip_percentage, total_bill):
    # Creating functions to help me in future situations. I'll need to carry a small raspberry pi with a
    # screen and keyboard to make my functions portable. I could use the 'Calculator' App, but I built
    # this with my hands... On to the problem.

    # Using the return function, I return the result of tip_percentage multiplied by total_bill
    return tip_percentage * total_bill

calculate_tip(.25, 100)


# ## 6.
# > Define a function named apply_discount.
# - It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[10]:


def apply_discount(original_price, discount_percentage):
    # I want to return the discounted price using the original price and discount_percentage

    # When discounting something, or reducing a value by a percentage. I can substract the
    # discounted percentage from 1, or 100%. I take the result of that vaule and multiply it
    # with original price to finc the discounted price.
    return original_price * (1-discount_percentage)

apply_discount(100, .25)


# ## 7.
# > Define a function named handle_commas. 
# - It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[15]:


def handle_commas(numeric_string):
    # The function accepts a string literal that contains numbers and commas.
    # Inside of the int() function. I use the replace string method on the
    # parameter 'numeric_string' to remove ALL commas and replace them with nothing - an
    # empty string. After removing the commas, I use the int() function to cast the
    # value from a string literal to a numeric literal. Progresso Chango. Soup.

    numeric_literal = int(numeric_string.replace(',',''))
    return numeric_literal

print(handle_commas('100,000,000'))
print(handle_commas('10,000,0000,000,0,0,0,0,00000')) # <- lol


# ## 8.
# > Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[21]:

# Ah yes, the get_letter_grade function. I use the if elif else clause to create boundaries. I think of it
# like a waterfall with many different collection 'pools' until the else clause, the collection 
# biggest 'pool' of all.

# I am able to progressively catch any letter grade value by organizing each if/elif/ clause to catch
# numbers directly above and directly below certain boundaries. Return None because of PEP 8.
def get_letter_grade(grade):
        if grade >= 90:
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
print(get_letter_grade(59.99999999999999999999)) # It actually rounds up to a D!?! Grade is not explicitly an int
print(get_letter_grade(-100))


# ## 9.
# > Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[25]:


def remove_vowels(word):
    # I initialize an empty string with an appropriately named variable. This variable
    # will hold all consonants that are contained in the string literal parameter word.
    word_with_removed_vowels = ''
    
    # I use the for x in y clause to look at each character of string literal parameter word.
    for letter in word:
        # If the letter is a consonant, then I want to concatenate that letter onto my empty
        #string variable 'word_with_removed_vowels'.
        if is_consonant(letter) == True:
            word_with_removed_vowels += letter
    # I don't need an elif/else clause here. If the letter is not a consonant, I don't want my
    # program to do anything. After the for... in... iteration ends, return the variable
    # 'word_with_removed_vowels'.
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

# In[191]:


import keyword
keyword.kwlist

def normalize_name(word):
    
    word = word.lower().lstrip("\"'~`1234567890~!@#$%^&*()_+[]\|}{};'\"?><").rstrip("!#@%$").replace(' ', '_')
    
    if word in keyword.kwlist:
        return "Come up with another variable name. That's a Python KEYWORD!"
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

# In[30]:


# Each iteration of index, I use index notation to slice the list of numbers
# into tiny bits. Every iteration, a list of numbers up to index i+1 is sliced
# from the original list of numbers.
# The sum function adds the sliced number list.
# Place that iterative process in a list comprehension and bam, a sequential
# sum of cumulative values! Gordon Ramsay would be impressed at the slicing
# speed of this function.
cumulative_sum = lambda sequence: [sum(sequence[:index+1]) for index in range(len(sequence))]


# In[31]:


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_numbers[:0+1]
cumulative_sum(list_of_numbers)


# # BONUS
# ## 1.
# > Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[155]:

# Ah, yes this exercise. Let's go on a journey...

def twelveto24(time_of_day):
    # I initialize an empty string to contain 24 hour time.
    clock_24_hours = ''
    
    # I use the string method lower() to lowercase any AM/PM values and assign it to variable 'time_of_day'
    time_of_day = time_of_day.lower()
    
    # If the length of the variable 'time_of_day' is 6 characters long, I know that the hour
    # hand is only 1 character in length. Any hour hand less than 10am/10pm.
    if len(time_of_day) == 6:
        # If the string contains 'am' I know it's mornin' time.
        if 'am' in time_of_day:
            # I concatenate a '0' string literal to variable 'time_of_day' with 'am' removed.
            clock_24_hours = '0' + time_of_day.rstrip('am')
            return clock_24_hours
        elif 'pm' in time_of_day:
            # If the time is less than 10pm, I want to add the numeric literal of index 0 + 12
            # I concatenate the 24 hour with the minutes from time_of_day with 'pm' removed.
            clock_24_hours = str(int(time_of_day[0]) + 12) + time_of_day[1:].rstrip('pm')
            return clock_24_hours
    
    # If the length of the characters in the parameter time_of_day is 7, I know the hour
    # hand is >= 10.
    elif len(time_of_day) == 7:
        if 'am' in time_of_day:
            if int(time_of_day[:2]) == 12:
                # If the time is 12 something. I convert 12-hr to '00' to denote the start of a new day.
                clock_24_hours = "00" + time_of_day[2:].strip('am')
            else:
                # if it's any other time than 12am, I remove am from the string
                clock_24_hours = time_of_day.rstrip('am')
                return clock_24_hours
        elif 'pm' in time_of_day:
            # If it is 12:xx pm, I want to remove 'pm'
            if int(time_of_day[:2]) == 12:
                clock_24_hours = time_of_day.rstrip('pm')
                return clock_24_hours
            else:
                # If the time is 'pm' I need to add 12 to the hour portion on time_of_day
                clock_24_hours = str(int(time_of_day[:2]) + 12) + time_of_day[2:].rstrip('pm')
                return clock_24_hours


# In[159]:


print(twelveto24('3:00pm'))
print(twelveto24('1:00pm'))

# ## 2.
# > Create a function named col_index. It should accept a spreadsheet column name, and
# return the index number of the column.

# In[208]:

# This one was fun. I got to use my whiteboard :).

# When I sat with the problem, it reminded me of combinations in probability. 
# Going through the Khan Academy prework for Codeup paid off. Thanks Khan Academy.
def col_index(column_name):
    # I initialize 3 variables
    # The first is to calculate the 'grouping' value of all columms excluding the last column
    column_group_value = 0
    # This variable is seperate because I'll need to calculate the last column sperately.
    last_column_value = 0
    # This variable stores the value of column_group_value and last_column_value
    total_column_value = 0


    # OMG. I making a cipher. lol.
    # Each letter in a column_name has value. Each letter from A-Z has values 1-26.
    # I use a dictionary to bind the letter and number together.
    letter_values = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
                     'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
                     'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,
                     'W':23,'X':24,'Y':25,'Z':26}
    
    # This is where I broke out the white board. Instead of adding 26 from each column
    # grouping, I need to calculate the product of 26 times the letter value at a certain
    # position. I add those values to column_group_value
    if len(column_name) >= 2:
        for letter in column_name[:len(column_name)-1]: 
            column_group_value += 26 * letter_values[letter]
  
    # This for in clause chops of the last column and evaluates it seperately.
    for letter in letter_values:
        if letter == column_name[-1]:
            last_column_value += letter_values[letter]
    
    # Return the fruits of my intellectual labor.
    total_column_value = column_group_value + last_column_value
    return total_column_value    


# In[217]:


col_index('ZA')



# %%
