### 1. Strings to DateTimes

# Import the datetime object from the datetime module
from datetime import datetime

# Iterate over the dates_list 
for date_str in dates_list:
    # Use the `.strptime()`[string parse time] method to parse a string into a datetime using a specified notation.
    # Convert each date to a datetime object: date_dt
    date_dt = datetime.strptime(date_str, '%m/%d/%Y')
    
    # Print each date_dt
    print(date_dt)


### 2. Converting to a String

# Loop over the first 10 items of the datetimes_list
for item in datetimes_list[:10]:
    # Use the `.strftime()` to format each string by a specified format.
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(datetime.strftime(item, '%m/%d/%Y'))
    
    # Print out the record as an ISO standard string
    print(datetime.isoformat(item))


### 3. Pieces of Time

# Create a defaultdict of an integer: monthly_total_rides
# Each key-value pair will contain an integer value
# Key: Month number: 1-12
# Value: The number of riders in a month
monthly_total_rides = defaultdict(int)

# Loop over the list daily_summaries
for daily_summary in daily_summaries:
    # Convert the service_date to a datetime object
    service_datetime = datetime.strptime(daily_summary[0], '%m/%d/%Y')

    # Add the total rides to the current amount for the month
    # Use the `.month` accessor to retrieve the month from the datetime stored in "service_datetime"
    monthly_total_rides[service_datetime.month] += int(daily_summary[4])
    
# Print monthly_total_rides
print(monthly_total_rides)


### 4. Creating DateTime Objects

# Import datetime from the datetime module
from datetime import datetime

# Compute the local datetime: local_dt
# Use datetime.now() function to retrieve the datetime NOW
local_dt = datetime.now()

# Print the local datetime
print(local_dt)

# Compute the UTC datetime: utc_dt
# Use the datetime.utcnow() to retrieve the datetime NOW in UTC or Universal Coordinated Time.
utc_dt = datetime.utcnow()

# Print the UTC datetime
print(utc_dt)


### 5. Timezones

# Import timezone from the pytz module
from pytz import timezone

# Create a Timezone object for Chicago
chicago_usa_tz = timezone('US/Central')

# Create a Timezone object for New York
ny_usa_tz = timezone('US/Eastern')

# Iterate over the daily_summaries list
for orig_dt, ridership in daily_summaries:

    # Make the orig_dt timezone "aware" for Chicago
    # Using a `.replace(tzinfo=*timezone*)` on a datetime object will give it a timezone!
    chicago_dt = orig_dt.replace(tzinfo=chicago_usa_tz)
    
    # Convert chicago_dt to the New York Timezone
    # With a datetime that is "timezone" aware, we can use `.astimezone()` to set the timezone to Eastern
    ny_dt = chicago_dt.astimezone(ny_usa_tz)
    
    # Print the chicago_dt, ny_dt, and ridership
    print('Chicago: %s, NY: %s, Ridership: %s' % (chicago_dt, ny_dt, ridership))


### 6. Finding a time in the Future and from the Past using TimeDelta

# Import timedelta from the datetime module
from datetime import timedelta

# Build a timedelta of 30 days: glanceback
# Create a timedelta object that is 30 days
glanceback = timedelta(30)

# Iterate over the review_dates as date
for date in review_dates:
    # Calculate the date 30 days back: prior_period_dt
    prior_period_dt = date - glanceback
    
    # Print the review_date, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (date, 
          daily_summaries[date]['day_type'], 
          daily_summaries[date]['total_ridership']))

    # Print the prior_period_dt, day_type and total_ridership
    print('Date: %s, Type: %s, Total Ridership: %s' %
         (prior_period_dt, 
          daily_summaries[prior_period_dt]['day_type'], 
          daily_summaries[prior_period_dt]['total_ridership']))



### 7. Finding Differences in DateTime

# Iterate over the date_ranges
for start_date, end_date in date_ranges:
    # Print the End and Start Date
    print(end_date, start_date)
    # Print the difference between each end and start date
    print(end_date - start_date)


### 8. Localizing Time with the Pendulum module

# Import the pendulum module
import pendulum

# Create a now datetime for Tokyo: tokyo_dt
tokyo_dt = pendulum.now('Asia/Tokyo')

# Covert the tokyo_dt to Los Angeles: la_dt
# Use the `.in_timezone()` method from the pendulum object to convert the time from Asia to America
la_dt = tokyo_dt.in_timezone('America/Los_Angeles')

# Print the ISO 8601 string of la_dt
print(la_dt.to_iso8601_string())


### 9. Humanizing Differences with Pendulum

# Iterate over date_ranges
for start_date, end_date in date_ranges:

    # Convert the start_date string to a pendulum date: start_dt
    # strict by default is True, which only accepts datetimes in isoformat
    start_dt = pendulum.parse(start_date, strict=False)
    
    # Convert the end_date string to a pendulum date: end_dt 
    end_dt = pendulum.parse(end_date, strict=False)
    
    # Print the End and Start Date
    print(end_dt, start_dt)
    
    # Calculate the difference between end_dt and start_dt: diff_period
    diff_period = end_dt - start_dt
    
    # Print the difference in days
    print(diff_period.in_days())