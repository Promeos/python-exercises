### 1. Manipulating Lists in Python

# Create a list of strings that contain baby names
# Create a list containing the names: baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# Extend the list `baby_names` with 2 new baby names.
# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(['Rowen', 'Sandeep'])

# Display the baby's names.
# Print baby_names
print(baby_names)

# Use python's built-in list method `.index` to find the position/index location of 'Aliza'
# Find the position of 'Aliza': position
position = baby_names.index('Aliza')

# Using Aliza's index stored in the variable position, remove Aliza from the list of baby names. 
# Remove 'Aliza' from baby_names
baby_names.pop(position)

# Display the list of baby names to show the list with Aliza removed.
# Print baby_names
print(baby_names)


### 2. Looping over Lists

# Create an empty list using bracket notation, [] and name the empty list `baby_names`
# Create the empty list: baby_names
baby_names = []

# Use a for loop to iterate through the list of lists named `records` and append the empty list
# with the baby's name which is stored the 4th element in the list.
# Loop over records 
for row in records:
    # Use python's built-on list method named `.append` to add a single element to a list.
    # Add the name to the list
    baby_names.append(row[3])
    
# Use Python's built-in `sorted()` function to sort the baby names alphabetically.
# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)


### 3. Data type usage

# Which data type would you use if you wanted your data to be immutable
# and ordered? TUPLE


### 4. Using and Unpacking Tuples

# Use Python's built-in zip function to create girl and boy name pairs via a tuple.
# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Use Python's `enumerate()` function to iterate each index and element in the tuple
# Iterate over pairs
for idx, pair in enumerate(pairs):
    # Each `pair` in the iterator is a tuple. Unpack the tuple into girl_name, boy_name variables.
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Use string formatting to print the index, girl name and boy name for each pair of names. 
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))


### 5. Making Tuples by Accident

# Create the normal variable: normal
normal = 'simple'

# CAUTION WIZARD: Strings or numbers with a trailing comma will transform the variable
# into a tuple!!!
# Create the mistaken variable: error
error = 'trailing comma',

# Print the types of the variables
# Returns <class 'str'>
print(type(normal))
# Returns <class 'tuple'>
print(type(error))


### 6. Finding all the data and the overlapping data between sets.

# Use Python's built-in set method `.union()` to find all names from both sets
# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
# Returns 1460, the union of names from 2011 and 2014
print(len(all_names))

# Use Python's built-in set method `.intersection()` to find baby names
# that are found in both the 2011 baby names and 2014 baby names.
# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
# Returns 987, the number of baby names found in both the 2011 and 2014 sets.
print(len(overlapping_names))


### 7. Determining Set Differences

# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Iterate through each row in `records`
    # Check if the first column is '2011'
    if row[0] == '2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3])

# Use Python's built-in set method `.difference()` to find the baby names that occur
# In the 2011 baby names set only.
# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)