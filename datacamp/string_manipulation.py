### 1. Find the Number of Characters in the String

# Find characters in movie variable
length_string = len(movie)


### 2. Select a Portion of a String

# Select the first 32 characters of movie1
first_part = movie1[:32]

# Select from 43rd character to the end of movie1
last_part = movie1[42:]

# Select from 33rd to the 42nd character
middle_part = movie2[32:42]

# Print concatenation and movie2 variable
print(first_part+middle_part+last_part) 
print(movie2)


### 3. Palindromes: Reversing a String

# Get the word
movie_title = movie[11:30]

# Obtain the palindrome
palindrome = movie_title[::-1]

# Print the word if it's a palindrome
if movie_title == palindrome:
	print(movie_title)


### 4. Text Normalization: `.lower()`

# Convert the movie review to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)


### 5. Replace, Join, and Splitting Strings

# Remove tags happening at the end and print results
movie_tag = movie.replace('<\i>', '')
print(movie_tag)

# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

# Join back together and print results
movie_join = ' '.join(movie_no_comma)
print(movie_join)


### 6. Split Lines or Split the Line

# Split string at line boundaries
file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(',')
    print(substring_split)


### 7. Finding Substrings

for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))


### 8. Locating a Word in a String using `.find()`

for movie in movies:
  # Find the first occurrence of word
  print(movie.find('money', 12, 51))

for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.index('money', 12, 51))
  except ValueError:
    print("substring not found")


### 9. Text Negation using `.replace()`

# Replace negations 
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)
