
import csv
    
    
# Empty dict to store data
data_dict = {}
    
# Read csv file
with open('Customer.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    
    # Convert each row into dict
    for row in reader:
        key = row['Id']
        del row['Id']
        data_dict[key] = row
    
print(data_dict['BOLID'])