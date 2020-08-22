#!/usr/bin/env python
# coding: utf-8

# # Tesseractbuster Movie Rentals

# In[1]:


# You have rented some movies for your kids: 
# The little mermaid (for 3 days), Brother Bear (for 5 days, 
# they love it), and Hercules (1 day, you don't know yet if they're 
# going to like it). If price for a movie per day is 3 dollars, 
# how much will you have to pay?

# create a dictionary of movies and number of days rented.
my_rented_movies = {'The Little Mermaid': 3,
                    'Brother Bear': 5,
                    'Hercules': 1}

# create a function to calculate the total rental fee.
def rental_fee(rented_movies):
    # create a variable for the rental fee to generalize the formula
    daily_rental_fee = 3
    
    # use a list comprehension to pull the number of days from each movie
    total_fee = sum([movie * daily_rental_fee for movie in rented_movies.values()])
    
    # create a message variable to generalize the message
    message = f'Your kiddos ran up a bill of ${total_fee}. More movies!'
    print(message)
    # return total_fee


# In[2]:


rental_fee(my_rented_movies)


# # Data Science Contract Work

# In[79]:


# Suppose you're working as a contractor for 3 companies:
# Google, Amazon and Facebook, they pay you a different rate per hour.
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350.
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

# Wowie that is amazing. To the problem at hand!

def data_scientist_contractor_pay():
    print("Welcome to the Data Science Contractor Pay Calculator."
          + "\n\nLet's see how much you earned this week.")
    
    google_hourly_rate = 400
    amazon_hourly_rate = 380
    facebook_hourly_rate = 350
    
    # generalize input functions to get hours worked from the user
    facebook_hours = float(input("Enter number of contract hours worked for Facebook: "))
    google_hours = float(input("Enter number of contract hours worked for Google: "))
    amazon_hours = float(input("Enter number of contract hours worked for Amazon: "))

    # create variables to calculate invoices to the FANGS
    invoice_to_google = google_hours                         * google_hourly_rate
        
    invoice_to_amazon = amazon_hours                         * amazon_hourly_rate
        
    invoice_to_facebook = facebook_hours                         * facebook_hourly_rate
    
    amount_earned_this_week = round(sum([invoice_to_google                                          + invoice_to_amazon                                          + invoice_to_facebook
                                        ]), 2)
    
    # create a variable to generalize the message
    message = f"\nYou earned ${amount_earned_this_week} this week. Wowie!"
    
    print(message)
    #return amount_earned_this_week

# call the function
data_scientist_contractor_pay()


# # Enrollment Eligibility

# In[83]:


# A student can be enrolled to a class only if the class is not full and the class 
# schedule does not conflict with her current schedule.
# This would be awesome to build out fully


# create a function to determine class eligibility
def enrollment_eligibility(person_schedule, class_limit):
    
    # create message variables for generalization
    name = input('Hello potential Dardenite! What is your name?: ').capitalize()
    
    message = ("It's nice to meet you {}! Let's see if you're"
               " eligible to enroll in our Bootcamp...\n").format(name)
        
    # display message to determine eligibility
    print(message)
    
    # create conditional variables to determine eligibility
    is_class_full = class_limit > 31
    schedule_is_open = person_schedule == True
    is_easter_egg = class_limit == 30 and schedule_is_open
    eligible_applicant = schedule_is_open and not is_class_full
    
    # create message variable to display as outcomes of the selection structure
    class_limit = ("I'm sorry {}. We don't have space in this Bootcamp."
                    "\nWould you like to be the first "
                    "applicant to the next cohort?").format(name)
    schedule_conflict = ("If your schedule doesn't fit us in right now"
                         " let's stay in touch, {}.").format(name)
    class_open_schedule_open = ("You're eligible! Here are 3 assessments"
                                " I'll need you to complete.")
    special_message = ("Well, {}. Call yourself Charlie because you've "
                       "got the last Golden Ticket to Darden!"
                       "\nHere are 3 assessments I'll need you"
                       " to complete...").format(name)
    formal_message = ("You're eligible! Here are 3 assessments I'll need you to complete.")
    
    # selection structure to determine eligibility
    if is_easter_egg:
        print(special_message)
    elif eligible_applicant:
        print(formal_message)
    elif not schedule_is_open:
        print(schedule_conflict)
    elif is_class_full:
        print(class_limit)   
    else:
        return None

#initialize variables
student_availability = True
current_cohort_applicants = 30

# run the function
enrollment_eligibility(student_availability, current_cohort_applicants)
    
    


# # Super Market Discount

# In[87]:


# A product offer can be applied only if people buys more than 2 items,
# and the offer has not expired.
# Premium members do not need to buy a specific amount of products.
# I secretly loved Super Market Sweep as a kid.


def is_premium_member():
    # create a variable to generalize the message
    question = "Are you a Ralph\'s Rewards member (y/n)?: "
    answer = input(question).lower()
    
    # create conditional variables to navigate the selection structure
    member = answer == 'y'
    potential_member = answer == 'n'
    
    # create variables to store responses
    prospect_member_script = ("\nWHAT?! YOU'RE NOT A REWARDS MEMBER?!\n"
                              "Would you like to become a Ralph's Rewards member?"
                              " It's the low, low price of: F. R. E. E...\n")

    catch_all = "\nA flash mob breaks out dancing to Thriller.\n"
    
    # determine if the customer is a member or potential member
    if member:
        return True
    elif potential_member:
        print(prospect_member_script)
        return False
    else:
        print(catch_all)
        return None

    
def product_offer(product_name, number_of_products, is_valid_offer,):
    #create a variable to generalize greeting script
    discount_script = ("Hello! How are you this fine day?"
                       "\n\n**Cashier checks out items. Happy beeping noises**"
                       "\n\nAh you've brought in a discount offer for {}.\n"
                       "Let's see if your eligible for the discount..."
                       "\n").format(product_name) 
    
    # print customary cashier greeting
    print(discount_script)
    
    # creating conditional variables I learned this from Ryan O. during the walkthrough! 
    # Sweet. Readability!
    premium_member = is_premium_member()
    eligible_number_of_products = number_of_products > 2
    good_coupon = is_valid_offer == True
    
    # store messages in variables for readability.
    premium_member_or_offer_valid = ("\nYou're eligible for a discount on your "
                                     f"{product_name}!")
        
    more_product_offer_valid = ("You're almost eligible for this discount!"
                                " You need more than 2 of the same item."
                                "\nI'll have a team member get it for you. Tony,"
                                " I have a BLUE LIGHT SPECIAL!")
        
    no_elibility = "I'm sorry you're not eligible for the discount."
    
    # selection structre incorporating conditional variables. My eyes are happy.
    if premium_member or (eligible_number_of_products and good_coupon):
        print(premium_member_or_offer_valid)
        
    elif good_coupon and not eligible_number_of_products:
        print(more_product_offer_valid)
        
    else:
        print(no_elibility)
        return None


# In[88]:


product = "Canned Yams"
quantity = 2
offer = True

product_offer(product, quantity, offer)


# # Password Exercise

# In[5]:


# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace


# create a username and password
username = 'codeup'
password = 'notastrongpassword'

# the password must be at least 5 characters
# the username must be no more than 20 characters
username_length = len(username) >= 5
password_length = len(password) <= 20

# bonus neither the username or password can start or end with whitespace
username_whitespace = username == username.strip()
password_whitespace = password == password.strip()

# the password must not be the same as the username
username_is_password = username == password

# variables to combine conditional expressions together
valid_username = username_length and username_whitespace and not username_is_password
valid_password = password_length and password_whitespace and not username_is_password
valid_credentials = valid_username and valid_password

print(valid_credentials)


# # Everything below this are data type experiments

# In[82]:


# this is a numeric literal of type float because of the decimal value
type(99.9)


# In[7]:


# this is a string literal because of the quotation marks. This will return
# type str
type("False")


# In[8]:


# this is a boolean value that will return type bool
type(False)


# In[9]:


# this is a string literal that returns type str
type('0')


# In[10]:


# this is a numeric literal that return type int
type(0)


# In[11]:


# this is a boolean value with a type bool
type(True)


# In[12]:


# this is a string literal of type str
type('True')


# In[15]:


# this is a list data type. Although a dict data type resides in the list
# the list data type 'contains' the dict value.
type([{'a': 'a'}])


# In[16]:


# this is a dict data type because the outer container is a dictionary
type({'a': []})


# What data type would best represent:
# 1. A term or phrase typed into a search box?
# > string data type 
# 
# 2. If a user is logged in?
# > boolean data type
# 
# 3. A discount amount to apply to a user's shopping cart?
# > float data type
# 
# 4. Whether or not a coupon code is valid?
# > boolean data type
# 
# 5. An email address typed into a registration form?
# > string data type
# 
# 6. The price of a product?
# > float data type
# 
# 7. A Matrix?
# > list data type
# 
# 8. The email addresses collected from a registration form?
# > dict data type
# 
# 9. Information about applicants to Codeup's data science program?
# > dict data type

# In[18]:


# This produces an error. Python cannot infer which data type to operate on.
# The string should be cast as an int or the int cast as a string depending on what
# the data presented or measured.
'1' + 2


# In[23]:


# This is the modulo operator! It performs division and returns the
# remainder of the dividend divided by the divisor. It will return 2.
6 % 4


# In[24]:


# this returns a data type of type int
type(6 % 4)


# In[1]:


# This returns an type error because Python cannot infer the
# from the command.
'3 + 4 is ' + 3 + 4


# In[3]:


# Evaluates to False because it is not greater than itself
0 < 0


# In[4]:


# Returns False because a string is not equal/ the exact value
# of a bool.
'False' == False


# In[6]:


# Returns False because a string is not equal/ the exact value
# of a bool.
True == 'True'


# In[7]:


# This evaluates to bool of True because 5 is greater than -5.
5 >= -5


# In[8]:


# I have never encountered this before.
get_ipython().system('False or False')


# In[9]:


# This is interesting. I have never used a boolean value in a
# conditional expression with a string!
True or "42"


# In[15]:


# When using a logical operator between two numeric literal the
# expression selects the lower of the two numeric literals!
42 or 210


# In[16]:


# Let's use a logical operator between strings. Interesting! It return the
# string with the smaller length.
"This is a string" or "This is a longer string"


# In[20]:


# Let's use a logical operator between string literals and numeric
# literals. Wow. Strings have precedent over numeric literals when using
# logical operators. Cool!
"1" or 50000000000


# In[21]:


# 
get_ipython().system('True && !False')


# In[22]:


# A modulo that will return the remainder of 6 / 5
6 % 5


# In[27]:


# This compound conditional expression evaluates to True
4 >= 0 and 1 == 1


# In[25]:


# This compound conditional expression evaluates to False
'codeup' == 'codeup' and 'codeup' == 'Codeup'


# In[28]:


# This exppression will raise a syntax error. The correct symbol
# for not equal is '!='
4 >= 0 and 1 !== '1'


# In[30]:


# This conditional expression evaluates to True because
# 6 divided by 3 leaves no remainder.
6 % 3 == 0


# In[31]:


# This expression evaluates to True because 5 divided by 2 leaves
# a remainder of 1 and that is not zero.
5 % 2 != 0


# In[35]:


# First time seeing this. This raises a Type Error because we cannot
# combine two different data types.
[1] + 2


# In[37]:


# This evaluates to a list with two elements 1, 2.
[1] + [2]


# In[40]:


# I did not know this! You can multiply a list by a scalar and
# the list will add elements according to the scalar.
[1] * 2


# In[43]:


# I have not seen this before. Before I executed the code I 
# hypothesized it would return a 2 x 2 matrix. Nope. Type Error
[1] * [2]


# In[45]:


# This evaluates to True because a empty list is exactly equal to
# an empty list
[] + [] == []


# In[47]:


# This will return a Type Error because dicts have their own
# 'addition' method.
{} + {}

