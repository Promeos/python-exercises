#!/usr/bin/env python
# coding: utf-8

# # 20 Python Data Structure Manipulation Exercises

# In[89]:


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# > # The following questions reference the `students` data structure above. Write the python code to answer the following questions:

# ### 1.
# > How many students are there?

# In[120]:


number_of_students = len(students)

print(f"There are {number_of_students} students.")


# ### 2. 
# > How many students prefer light coffee? For each type of coffee roast?

# In[121]:


def coffee_preference_of_students(students):
    coffee_preference_data = {
    'light' : len([s["coffee_preference"] for s in students if(
    s['coffee_preference'] == "light")]),
    'medium' : len([s["coffee_preference"] for s in students if(
    s['coffee_preference'] == "medium")]),
     'dark' : len([s["coffee_preference"] for s in students if(
    s['coffee_preference'] == "dark")])
    }
    
    return coffee_preference_data

coffee_preference_count = coffee_preference_of_students(students)
print(f"Student coffee preferences {coffee_preference_count}")


# ### 3.
# > How many types of each pet are there?

# In[122]:


pet_types = {}

for student in students:
    for animal in student['pets']:
        if animal['species'] not in pet_types:
            pet_types[animal['species']] = 1
        else:
            pet_types[animal['species']] += 1

for animal, count in pet_types.items():
    print(animal, count)


# ### 4.
# > How many grades does each student have? Do they all have the same number of grades?

# In[123]:


for student in students:
    for key in student:
        if key == 'grades':
            print(('{:>20}: {} grades').format(student['student'], len(student['grades'])))


# ### 5.
# > What is each student's grade average?

# In[124]:


def grade_average(list_of_numbers):
    return sum(list_of_numbers)/len(list_of_numbers)

for student in students:
    for key in student:
        if key == 'grades':
            print(('{:>20} grade average: {}').format(student['student'], 
                                                      grade_average(student['grades'])))


# ### 6.
# > How many pets does each student have?

# In[125]:


for student in students:
    for key in student:
        if key == 'pets':
            if len(student['pets']) < 2 and len(student['pets']) > 0:
                print(("{:>20} has {} pet").format(student['student'] ,
                                                   len(student['pets'])))
            else:
                print(("{:>20} has {} pets").format(student['student'] ,
                                                    len(student['pets'])))


# ## 7.
# > How many students are in web development? data science?

# In[126]:


course_types = [s['course'] for s in students]
enrolled_in_data_science = course_types.count('data science')
enrolled_in_web_development = course_types.count('web development')

print(f"Number of students enrolled in data science: {enrolled_in_data_science}")
print(f"Number of students enrolled in web development: {enrolled_in_web_development}")


# ### 8
# > What is the average number of pets for students in web development?

# In[127]:


web_development_pets = len(
    [s['pets'] for s in students if s['course'] == 'web development'])

avg_num_of_pets_web_dev = web_development_pets / enrolled_in_web_development

print(f"Average number of pets for web development students: {avg_num_of_pets_web_dev}")


# ### 9.
# > What is the average pet age for students in data science?

# In[128]:


ds_pet_ages = []

for student in students:
    if student['course'] == 'data science':
        for age in student['pets']:
            ds_pet_ages.append(age['age'])
        
average_ds_pet_age = round(sum(ds_pet_ages)/len(ds_pet_ages), 2)

print(f"Average pet age for data science students: {average_ds_pet_age} years")


# ### 10.
# > What is most frequent coffee preference for data science students?

# In[129]:


# Here I practice importing a module - collections module
from collections import Counter

get_ipython().run_line_magic('pinfo', 'Counter')


# In[130]:


# I can use the Counter function to return the elements from a list
# as a dictionary:
# key = `coffee_preference` - the element in the list
# value = roast type - number of times element appears in a list
# I encapsulate the Counter function in the dict() function to cast Counter -> dict
ds_coffee_pref_freq = dict(Counter([s['coffee_preference'] for s in students if(
s['course'] == 'data science')]))

# Once I filter the data for coffee preferences held by data science students
# with a for each coffee preference I can print the results
# print((ds_coffee_pref_freq))

print(("Most frequent coffee preference for data science students: {} --- dark").format(
    ds_coffee_pref_freq['dark']))


# ### 11.
# > What is the least frequent coffee preference for web development students?

# In[106]:


# Using the Counter function to create another frequency dict
wd_coffee_pref_freq = dict(Counter([s['coffee_preference'] for s in students if(
s['course'] == 'web development')]))

# Once I filter the data for coffee preferences held by web dev. students
# with a count for each coffee preference I can print the results
# print(wd_coffee_pref_freq)

print(("The least frequent coffee preference for web development students:\n"
       "{} medium\n"
       "{} dark").format(
    wd_coffee_pref_freq['medium'], wd_coffee_pref_freq['dark'])
     )


# ### 12.
# > What is the average grade for students with at least 2 pets?

# In[136]:


students_with_at_least_two_pets = [sum(s['grades']) for s in students if(
len(student['pets']) <= 2)]

avg_grade_of_students_with_2_pets = round(
    sum(students_with_at_least_two_pets)
    / (len(students_with_at_least_two_pets) 
    * 4)
    ,2)

print(("Average grade for students with two pets: {}").format(
    avg_grade_of_students_with_2_pets))


# ### 13.
# >How many students have 3 pets?

# In[103]:


num_students_with_3_pets = len([s for s in students if(
len(s['pets']) == 3)])
print("Number of students with 3 pets: {}".format(students_with_3_pets))


# ### 14.
# > What is the average grade for students with 0 pets?

# In[110]:


avg_grade_0_pets = sum([sum(s['grades']) for s in students if(
len(s['pets']) == 0)]) / 8

print("Average grade for students with 0 pets: {}".format(
    round(avg_grade_0_pets, 2)))


# ### 15.
# > What is the average grade for web development students? data science students?

# In[66]:


wd_student_grades = [sum(s['grades']) for s in students if(
s['course'] == 'web development')]

wd_grade_average = (sum(wd_student_grades)
                    / (enrolled_in_web_development
                    * 4)
                   )

ds_student_grades = [sum(s['grades']) for s in students if(
s['course'] == 'data science')]

ds_grade_average = (sum(ds_student_grades)
                    / (enrolled_in_data_science
                    * 4)
                   )
print("Average grade for Web Development students: {}".format(
round(wd_grade_average, 2)))
print("Average grade for Data Science students: {}".format(
round(ds_grade_average, 2)))


# ### 16.
# > What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?

# In[79]:


grades_dark_coffee = [s['grades'] for s in students if(
s['coffee_preference'] == 'dark')]

grade_avg_dark_coffee = [sum(s['grades'])/len(s['grades']) for s in students if(
s['coffee_preference'] == 'dark')]

min_grade_avg_dark = min(grade_avg_dark_coffee)
max_grade_avg_dark = max(grade_avg_dark_coffee)
grade_avg_range_dark = max_grade_avg_dark - min_grade_avg_dark
print("Dark coffee drinkers: Max average grade {}, Min average grade {}".format(
max_grade_avg_dark, min_grade_avg_dark))
print("Average grade range for dark coffee drinkers: {}".format(
grade_avg_range_dark))


# ### 17.
# > What is the average number of pets for medium coffee drinkers?

# In[85]:


num_of_pets_med_coffee = [len(s['pets']) for s in students]
avg_num_of_pets_med_coffee = (sum(num_of_pets_med_coffee)
                             // len(num_of_pets_med_coffee))

print("Average number of pets for medium coffee drinkers: {}".format(
    avg_num_of_pets_med_coffee))


# ### 18.
# > What is the most common type of pet for web development students?

# In[159]:


wd_pets = {}

for student in students:
    if student['course'] == 'web development':
        for animal in student['pets']:
            if animal['species'] not in wd_pets:
                wd_pets[animal['species']] = 1
            else:
                wd_pets[animal['species']] += 1

# for animal, count in wd_pets.items():
#     print(animal, count)

print("Most common type of pet for Web"
      " Development students:\n{} {}".format(
          'horse',
          wd_pets['horse']))


# ### 19.
# > What is the average name length?

# In[168]:


length_of_names = [len(s['student']) for s in students]
avg_name_length = sum(length_of_names) // len(length_of_names)

print(f"Average name length: {avg_name_length} letters")


# ### 20.
# > What is the highest pet age for light coffee drinkers?

# In[177]:


pets_light_coffee = []

for student in students:
    if student['coffee_preference'] == 'light':
        for animal in student['pets']:
           pets_light_coffee.append(animal['age'])
oldest_pet_light_coffee = max(pets_light_coffee)
print(f"The highest pet age for light coffee drinkers: {oldest_pet_light_coffee}yrs old")

