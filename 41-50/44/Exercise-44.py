
import csv
import json
    
    
data_dict = {}
    
# Read csv file
with open('Customer.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    
    # Convert each row into dict
    for row in reader:
        key = row['Id']
        del row['Id']
        data_dict[key] = row
    
# Write to JSON file
with open('customer.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data_dict, indent=4))