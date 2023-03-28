
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