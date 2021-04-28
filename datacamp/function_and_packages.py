### 1. Basic Functions: Print, Type, Len, int
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)


### 2. Joining Lists and Sorting the Values
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Use the `+` operator to join two lists together
# Paste together first and second: full
full = first + second

# Use Python's built-in `sorted(reverse=False)` function to sort the values in a list.
# reverse = False : Sort values in Ascending order.
# reverse = True : Sort values in Descending order.

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)


### 3. String Functions
# string to experiment with: place
place = "poolhouse"

# Use str built-in function `.upper` to capitalize all characters in a string.
# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place, place_up)

# Use str built-in method `.count` to count the number of times a character appears in a string.
# Print out the number of o's in place
print(place.count('o'))


### 4. List Functions
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use list's built-in method `.index` to return the index position of a value.
# Print out the index of the element 20.0
print(areas.index(20.0))

# Use list's built-in method `.count` to count the number of times a value appears in a list.
# Print out how often 9.50 appears in areas
print(areas.count(9.50))


### 5. Updating Lists
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use lists built-in method `.append` to add a single element to the end of a list.
# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Use lists built-in method `.reverse` to reverse the order of elements in a list.
# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)


### 6. Importing Packages
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


### 7. Selective Imports
# Definition of radius
r = 192500

# Select the `randians` function from the `math` package.
# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)