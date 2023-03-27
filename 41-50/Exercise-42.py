# The file Customer.csv (utf-8 coding) containing data about the customers of a certain application is attached to the exercise.


# Load Customer.csv and extract all unique country names sorted alphabetically as a list and assign to unique_countries. Print the contents of the unique_countries variable to the console.


# In the solution, use the built-in csv module.


# csv documentation: https://docs.python.org/3/library/csv.html


# Expected result:


#     ['Argentina', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Denmark', 'Finland', 'France', 'Germany', 'Ireland', 'Italy', 'Mexico', 'Norway', 'Poland', 'Portugal', 'Spain', 'Sweden', 'Switzerland', 'UK', 'USA', 'Venezuela']

import csv
    
    
# Read csv file
with open('Customer.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = tuple(reader)
    
# Extract index for Country column
country_idx = columns.index('Country')
    
# Extract all Country names
countries = [row[country_idx] for row in rows]
    
# Extract all sorted unique country names
unique_countries = sorted(set(countries))
print(unique_countries)