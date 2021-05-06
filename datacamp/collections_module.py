### 1. Using Counter on lists

# Import the Counter object from the collections module.
from collections import Counter

# Print the first ten items from the stations list
# Using slice notation
print(stations[:10])

# Create a Counter of the stations list: station_count
# Counter creates a dict like object with the element as the key, and the number of times it occurs in the list as the value.
station_count = Counter(stations)

# Print the station_count
print(station_count)


### 2. Finding Most Common Elements

# Import the Counter object from the collections module
from collections import Counter

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Use the `.most_common()` method to return the n most common elements in a list/collection
# Find the 5 most common elements
print(station_count.most_common(5))


### 3. Creating Dictionaries of an Unknown Structure

# Create an empty dictionary: ridership
ridership ={}

# Iterate over the entries (dtype=tuple)
for date, stop, riders in entries:
    # Check to see if date is already in the ridership dictionary
    # Use the `in` keyword to determine if the date is a key in the dictionary named "ridership"
    if date not in ridership:
        # Create an empty list for any missing date: key-value pair
        ridership[date] = []
    # Append the stop and riders as a tuple to the date keys list
    ridership[date].append((stop, riders))
    
# Print the ridership for '03/09/2016'
print(ridership.get('03/09/2016'))


### 4. Safely Appending to a Key's value list

# Import defaultdict from the collections module.
from collections import defaultdict

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date, stop, riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)
    
# Print the first 10 items of the ridership dictionary
print(list(ridership.items())[:10])


### 5. Working with OrderedDictionaries

# Import OrderedDict from the collections module
from collections import OrderedDict

# Create an OrderedDict called: ridership_date
ridership_date = OrderedDict()

# Iterate over the entries
for date, riders in entries:
    # If a key does not exist in ridership_date, set it to 0
    if  date not in ridership_date:
        ridership_date[date] = 0
        
    # Add riders to the date key in ridership_date
    ridership_date[date] += riders
    
# Print the first 31 records
print(list(ridership_date.items())[:31])


### 6. Powerful Ordered Popping

# Use index notation to locate the first key from the list of keys in the dict "ridership_date"
# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Use the `.popitem()` method to remove the first key-value pair in "ridership_date"
# Pop the first item from ridership_date and print it
print(ridership_date.popitem(0))

# Use index notation to return the last key from the list of keys
# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])

# Use the `.popitem()` method to remove the last key-value pair in "ridership_date"
# Pop the last item from ridership_date and print it
print(ridership_date.popitem(-1))


### 7. Creating namedtuples for Storing Data

# Import namedtuple from the collections module
from collections import namedtuple

# So freakin' awesome!!!
# Create the namedtuple: DateDetails
# Create a container called 'DateDetails' that accepts 3 name attribute to capture rider information.
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over each tuple in "entries" list
for date, stop, riders in entries:
    # Append a new DateDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(DateDetails(date, stop, riders))
    
# Print the first 5 items in labeled_entries
print(labeled_entries[:5])


### 8. Leveraging Attributes on namedtuples

# Iterate over the first twenty items in labeled_entries
# Each item in "labeled_entries" is a namedtuple object with named attributes!!! 
for item in labeled_entries[:20]:
    # Print each item's stop using the attribute .stop
    print(item.stop)

    # Print each item's date using the attribute .date
    print(item.date)

    # Print each item's riders using the attribute .riders
    print(item.riders)