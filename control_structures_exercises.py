#!/usr/bin/env python
# coding: utf-8

# ## 1. Conditional Basics
# 
# > __A__. Prompt the user for a day of the week, print out whether the day is Monday or not.

# In[36]:


question = "Top of the morning young person, is it Monday? (y/n): "
response = input(question)

is_monday = response.lower() == 'y'

if is_monday:
    print("It's Monday!")
else:
    print("It's not Monday")


# > __B__. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend.

# In[40]:


question = "Top of the morning young person, what day of the week is it?: "
response = input(question)

is_weekend = response.lower() in ('saturday', 'sunday')

if is_weekend:
    print("It's a weekend. DO WORK. ADD. COMMIT. PUSH. REPEAT")
elif not is_weekend:
    print("It's a week day. DO WORK. ADD. COMMIT. PUSH. REPEAT")
else:
    return None


# > __C__. Create variables and make up values for
#     - the number of hours worked in one week
#     - the hourly rate
#     - how much the week's paycheck will be

# In[47]:


number_of_hours = 60
HOURLY_RATE = 400

weekly_paycheck = number_of_hours * HOURLY_RATE

print(f"Your gross earnings this week: ${weekly_paycheck}. **Happy crying noises")


# > __D__. Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[50]:


over_time = (number_of_hours - 40) * (1.5 * HOURLY_RATE)
over_40_hours = number_of_hours > 40

weekly_paycheck_with_over_time = weekly_paycheck + over_time

if over_40_hours:
    print(f'${weekly_paycheck_with_over_time}')
else:
    print(f'{weekly_paycheck}')


# ## 2. Loop Basics
# 
# > A. While
#     - Create an integer variable i with a value of 5.
#     - Create a while loop that runs so long as i is less than or equal to 15
#     - Each loop iteration, output the current value of i, then increment i by one.

# In[31]:


i = 5

# I learned about one line while statements. It reads like a sentence.
# ZOP: I will use this syntax for readability. Flat is better than nested.
while i <= 15: print(i); i += 1


# > -Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[32]:


# create a variable to store starting value
number = 0

while number < 101:
    if number % 2 == 0:
        print(number)
    number += 1


# > Alter your loop to count backwards by 5's from 100 to -10.

# In[35]:


number = 100

while number > -11 and number < 101:
    if number % 5 == 0:
        print(number)
    # This while loop will always be divisible by 5 because the starting
    # variable is a multiple of 5. I'm questioning indenting the subtraction assignment
    # to fit inside the if statement.
    number -= 5


# In[12]:


# I learned something new!
# number = 100

# If I assign a compound conditional statement to a variable, it stores the condition
# A while loop only 'sees' while True or while False! Cue infinite loops.
# is_in_between = number > -11 and number < 101

# while is_in_between
#     if number % 5 == 0:
#         print(('{}\n').format(number))
#     number -= 5


# > Create a while loop that starts at 2, and displays the number squared on each line while
# the number is less than 1,000,000. Output should equal:

# In[29]:


number = 2
MAX_LIMIT = 1_000_000

while number < MAX_LIMIT: print(number); number **= 2


# In[30]:


number = 100

while number > 0: print(number); number -= 5


# > B. For Loops
# 
# > Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# In[49]:


question = 'Enter a number 1-10: '
response = int(input(question))

for i in range(1,11):
    print(f"{response} X {i} = {response*i}")


# > Create a for loop that uses print to create the output shown below. 

# In[47]:


for i in range(1, 10): print(str(i)*i)


# > C. break and continue
# 
# > Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# In[48]:


prompt = "Enter an odd number between 1 and 50: "

while True:
    number = input(prompt)
    
    if number.isdigit():
        number = int(number)
        if number > 1 and number < 50 and number % 2 != 0:
            print(("\nNumber to skip is: {}\n").format(number))
            for i in range(1, 50):
                if i == number:
                    print(f"Zoinks! Skipping number {number}")
                elif i % 2 != 0:
                    print(f"Here is an odd number: {i}")
            break
        else:
            continue
    else:
        continue


# > __d__. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[45]:


prompt = "Enter a positive number: "

while True:
    number = input(question)
    
    if number.isdigit() == True and int(number) > 0:
        number = int(number)
        for i in range(0, number + 1):
            print(i)
        break
    else:
        continue


# > __e__. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[69]:


question = "Enter a number: "

while True:
    number = input(question)
    
    if number.isdigit() == True and int(number) > 0:
        number = int(number)
        for reducer in range(0, number):
            print(number - reducer)
        break
    else:
        continue


# ## 3. Fizzbuzz
# 
# > One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by __Imran Ghory__, the test is designed to test basic looping and conditional logic skills.
# 
# > Write a program that prints the numbers from 1 to 100.
# 
# > For multiples of three print "Fizz" instead of the number
# 
# > For the multiples of five print "Buzz".
# 
# > For numbers which are multiples of both three and five print "FizzBuzz".

# In[1]:


for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')


# ## 4. Display a table of powers.
# 
# > Prompt the user to enter an integer.
# 
# >Display a table of squares and cubes from 1 to the value entered.
# 
# > Ask if the user wants to continue.
# 
# > Assume that the user will enter valid data.
# 
# > Only continue if the user agrees to.
# 

# In[31]:


prompt = "Let's get mathematical. Enter a number: "

while True:
    number = input(prompt)
    
    if number.isdigit() and int(number) > 0:
        number = int(number)

        number_header_length = len('number')
        squared_header_length = len('squared')
        cubed_header_length = len('cubed')

        table_format = "{{:<{a}}} | {{:<{b}}} | {{:<{c}}}".format(
            a=number_header_length,
            b=squared_header_length,
            c=cubed_header_length
            )
        
        print('\nTable of squared and cubed numbers.\n')
        print((table_format).format('number',
                                    'squared',
                                    'cubed'
                                    ))
        print((table_format).format('-'*number_header_length,
                                    '-'*squared_header_length,
                                    '-'*cubed_header_length
                                    ))

        for i in range(1, number+1):
            print((table_format).format(i, i**2, i**3))
        break
    else:
        continue


# ## 5. Convert given number grades into letter grades.
# - Prompt the user for a numerical grade from 0 to 100.
# - Display the corresponding letter grade.
# - Prompt the user to continue.
# - Assume that the user will enter valid integers for the grades.
# - The application should only continue if the user agrees to.
# 
# >Grade Ranges:
#  A : 100 - 88
#  B : 87 - 80
#  C : 79 - 67
#  D : 66 - 60
#  F : 59 - 0

# In[43]:


prompt = "Enter a grade from 0-100: "
recalculate = 'y'

while recalculate == 'y':
    grade = input(prompt)
    
    is_between_zero_and_hundred = int(grade) >= 0 and int(grade) <= 100
    
    if grade.isdigit() and is_between_zero_and_hundred:
        grade = int(grade)
        if grade >= 99:
            print(f"The letter grade for {grade} is A+")
        elif grade >= 88:
            print(f"The letter grade for {grade} is A-.")
        elif grade >= 86:
            print(f"The letter grade for {grade} is B+.")
        elif grade >= 80:
            print(f"The letter grade for {grade} is B-.")
        elif grade >= 78:
            print(f"The letter grade for {grade} is C+.")
        elif grade >= 67:
            print(f"The letter grade for {grade} is C-.")
        elif grade >= 65:
            print(f"The letter grade for {grade} is D+.")
        elif grade >= 60:
            print(f"The letter grade for {grade} is D-.")
        elif grade >= 0:
            print(f"The letter grade for {grade} is F.")
            
        response = input("\nWould you like to calcualte another grade? (y/n): ")
        
        if response.lower() == recalculate:
            continue
        else:
            print("\nEnding grade calculations...")
            recalculate = response
        
    else:
        continue


# ## 6. Create a list of dictionaries where each dictionary represents a book that you have read.
# 
# > Each dictionary in the list should have: keys title, author, and genre. 
# 
# > Loop through the list and print out information about each book.
# 
# > Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
# 
# 

# In[16]:


personal_library = [{'title':'Be Here Now', 'author':'Ram Dass', 'genre': 'Spirituality'},
                    {'title':'Super Mind', 'author':'Norman E. Rosenthal', 'genre': 'Self Help'},
                    {'title':'Anthem', 'author':'Ayn Rand', 'genre': 'Science Fiction'},
                    {'title':'Strength In Stillness', 'author':'Boss Ross', 'genre': 'Self Help'},
                    {'title':'As a Man Thinketh', 'author': 'James Allen', 'genre': 'Self Help'},
                    {'title':'Think and Grow Rich', 'author':'Napoleon Hill', 'genre': 'Self Help'},
                    {'title':'Cat\'s Cradle', 'author':'Kurt Vonnegut', 'genre': 'Science Fiction'},
                    {'title':'Breakfast of Champions', 'author':'Kurt Vonnegut', 'genre': 'Science Fiction'},
                    {'title':'The Sirens on Titan', 'author':'Kurt Vonnegut', 'genre': 'Science Fiction'},
                    {'title':'Slaughter House V', 'author':'Kurt Vonnegut', 'genre': 'Science Fiction'},
                    {'title':'The Power of Habit', 'author':'Charles Duhihgg', 'genre': 'Self Help'},
                    {'title':'Watchmen', 'author':'Alan Moore', 'genre': 'Science Fiction'},
                    {'title':'Elon Musk', 'author':'Ashlee Vance', 'genre': 'Biography'},
                    {'title':'Steve Jobs', 'author':'Walter Isaacson', 'genre': 'Biography'},
                   ]

                    
prompt = 'Enter a book genre: '                    
request = input(prompt)
request = request.lower()
print(f'Here are all the titles in the genre: {request.title()}')

listing_no = 0
for book in personal_library:
    if request == (book['genre']).lower():
        listing_no += 1
        print(('{}. {}').format(listing_no, book['title']))
