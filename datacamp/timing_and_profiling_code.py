### 1. Using %timeit

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
# Unpacking the range iterator is faster
nums_unpack = [*range(51)]
print(nums_unpack)


### 2. What is the correct syntax when using %timeit and
# only using 5 runs with 25 loops per each run?
# Answer: %timeit -r5 -n25 set(heroes)


### 3. Using  %timeit: Formal name or Literal Syntax
# Literal Syntax performs faster

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))


### 4. Using Cell Magic Mode (%%timeit)

hero_wts_lbs = []

for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)

wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462


### 5. Bringing it all Together: Star Wars profiling

# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, desired_publisher='George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, desired_publisher='George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))


### Pop quiz: steps for using %lprun

# Suppose you have a list of superheroes (named heroes) along with each hero's
# height (in centimeters) and weight (in kilograms) loaded as NumPy arrays
# (named hts and wts respectively).

def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

# What are the necessary steps you need to take in order to profile the convert_units()
# function acting on your superheroes data if you'd like to see line-by-line runtimes?

# Answer
# Use %load_ext line_profiler to load the line_profiler within your IPython session.

# Use %lprun -f convert_units convert_units(heroes, hts, wts) to get line-by-line runtimes.


### Pop quiz: steps for using %mprun

# Suppose you have a list of superheroes (named heroes) along with each hero's
# height (in centimeters) and weight (in kilograms) loaded as NumPy arrays
# (named hts and wts, respectively). You also have a convert_units() function saved
# in a file titled hero_funcs.py.

# What are the necessary steps you need to take in order to profile the
# convert_units() function acting on your superheroes data if you'd like to
# see the line-by-line memory consumption of convert_units()?

# Answer
# Use the command from hero_funcs import convert_units
# to load the function you'd like to profile.

# Use %load_ext memory_profiler to load the memory_profiler within your IPython session.
# press

# Use %mprun -f convert_units convert_units(heroes, hts, wts) to get
# line-by-line memory allocations.