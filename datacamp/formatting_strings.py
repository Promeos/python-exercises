### 1. Text Normalization

# Assign the substrings to the variables
# Normalize the strings from both sliced indexes using `.lower()`
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders 
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

# Use format to print strings
for my_string in my_list:
  	print(my_string.format(first_pos, second_pos))


### 2. Formatting Strings Displayed using `.format()`

# Create a dictionary
plan = {
        "field": courses[0],
        "tool": courses[1]
        }

# Complete the placeholders accessing elements of field and tool keys in the data dictionary
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

# Use the plan dictionary to replace placeholders
# When we pass a dictionary to the `data` argument, we can use bracket notation to select the value at a specific key
print(my_message.format(data=plan))


### 3. Using Datetime Objects in Strings

# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Format date
print(message.format(today=get_date))


### 4. Literal Formatting using f-strings

# Complete the f-string
# Using !r in f-string notation formats the variable into a raw string.
# Using :d in f-string notation formats the variables as numeric string.
print(f"Data science is considered {field1!r} in the {fact1:d}st century")

# Complete the f-string
# Using :e in f-string notation formats numeric values in scientific notation.
print(f"About {fact2:e} of {field2} in the world")

# Complete the f-string
# Using :.(n)f formats the decimal place of a numeric value. n is the number of decimal places to display 
print(f"{field3} create around {round(fact3, 2)}% of the data but only {fact4:.1f}% is analyzed")


### 5.

# Divide the length of list by 120 rounded to two decimals
print(f"Only {len(list_links)*100/120:.2f}% of the posts contain links")

# Replace the substring https by an empty string
print(f"{string1.replace('https', '')}")

# Include both variables and the result of dividing them 
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1/number2:.1f} tweets per min")