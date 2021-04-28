### 1. Creating a Numpy array
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))


### 2. Use NumPy broadcasting to calculate the height of the baseball players in meters.
# height is available as a regular list
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)


### 3. Use Numpy broadcasting to calculate:
# 1. Convert the heights of the baseball players from inches to meters
# 2. Convert the weights of the baseball players from pounds to kilograms
# 3. Calculate the BMI of each player

# height and weight are available as regular lists
# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / (np_height_m ** 2)

# Print out bmi
print(bmi)


### 4. Use a boolean numpy array to find the baseball players with a BMI less than 2
# 1
# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array: boolean array of True and False values evaluated using
# a conditional expression.
light = bmi < 21

# Print out light: numpy boolean array.
print(light)

# Use the Numpy boolean array named `light` as an index to BMI
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])


### 5. Subsetting NumPy Arrays
# height and weight are available as a regular lists
# Import numpy
import numpy as np

# `np.array()` converts the lists into NumPy Arrays
# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Use index/subset notation to return the baseball players weight at index 50
# Print out the weight at index 50
print(np_weight_lb[50])

# Use slice/subset notation to return a sub-array of baseball players weights at index 100 to 110(including)
# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])


### 6. Creating a 2 Dimensional NumPy Array
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Passing a list of lists to `np.array()` creates a 2-Dimensional NumPy array.
# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
# Returns <class 'numpy.ndarray'>
print(type(np_baseball))

# Print out the shape of np_baseball
# Returns a tuple (4, 2) 4 rows, 2 columns
print(np_baseball.shape)


### 7. Create a 2-Dimensional Dataset from a list of lists using NumPy
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Passing a list of lists to `np.array()` created an ndarray
# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
# Returns the tuple (1015, 2) 1015 rows, 2 columns
print(np_baseball.shape)


### 8. Subsetting a 2-Dimensional NumPy Array
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Transform the baseball data from a list of lists to a NumPy array.
# Create np_baseball (2 cols) column1 = 'heights', column2 = weights
np_baseball = np.array(baseball)

# Use subset notation to retrieve the 50th row of data from `np_baseball`.
# Print out the 50th row of np_baseball
print(np_baseball[49])

# Use subset notation to retrieve the 2nd column of data from `np_baseball`.
# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# Use subset notation to retrieve the weight of the 124th player in the dataset.
# Print out height of 124th player
print(np_baseball[123, 0])


### 9. Arithmetic Operations using NumPy Arrays.
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols) col1 = heights(in), col2 = weights(lbs), col3 = age(yrs)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = [0.0254, 0.453592, 1]

# Multiply a list of conversion values with the baseball dataset.
# Print out product of np_baseball and conversion
print(np_baseball * conversion)


### 10. Basic Statistics using NumPy
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height_in from np_baseball: col1 = heights 
np_height_in = np_baseball[:, 0]

# Use NumPy's built-in `.mean()` method to calculate the average height of the players
# in the dataset.
# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Use NumPy's built-in `.median()` method to return the height at the 50th percentile.
# Print out the median of np_height_in
print(np.median(np_height_in))


### 11. Baseball Players Statistics
# np_baseball is available

# Import numpy
import numpy as np

# Use NumPy's built-in method `.mean()` to calculate the average height of a baseball player.
# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Use NumPy's built-in method `.median()` to calculate the height at the 50th percentile.
# Print median height.
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Use NumPy's built-in method `.std()` to calculate the spread of heights from the mean - Standard Deviation.
# Print out the standard deviation on height.
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Use NumPy's built-in method `.corrcoef()` to calculate pearson's R
# of heights and weights for baseball players.
# Print out correlation between first and second column.
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))


### 12. Putting it All Together
# heights and positions are available as lists
# Import numpy
import numpy as np

# Convert the lists of lists into NumPy Arrays.
# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Use a boolean mask to filter heights that belong to goal keepers, indicated as 'GK'.
# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Use a boolean mask to return the heights of all players that ARE NOT goal keepers.
# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Use NumPy's built-in `.median()` method to calculate the median height of goal keepers
# Convert the value to a string a print it to the console
# Print out the median height of goalkeepers.
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Calculate the median height of all players that ARE NOT goal keepers.
# Convert the numeric value to a string and print it to the console.
# Print out the median height of other players.
print("Median height of other players: " + str(np.median(other_heights)))
