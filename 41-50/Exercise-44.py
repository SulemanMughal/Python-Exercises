# The file Customer.csv (utf-8 coding) containing data about the customers of a certain application is attached to the exercise.

# Convert the Customer.csv file to a JSON file named customer.json.

# First few users of customer.json (indent level - 4):


#     {
#         "ALFKI": {
#             "CompanyName": "Alfreds Futterkiste",
#             "ContactName": "Maria Anders",
#             "ContactTitle": "Sales Representative",
#             "Address": "Obere Str. 57",
#             "City": "Berlin",
#             "Region": "Western Europe",
#             "PostalCode": "12209",
#             "Country": "Germany",
#             "Phone": "030-0074321",
#             "Fax": "030-0076545"
#         },
#         "ANATR": {
#             "CompanyName": "Ana Trujillo Emparedados y helados",
#             "ContactName": "Ana Trujillo",
#             "ContactTitle": "Owner",
#             "Address": "Avda. de la Constituci\u00f3n 2222",
#             "City": "M\u00e9xico D.F.",
#             "Region": "Central America",
#             "PostalCode": "05021",
#             "Country": "Mexico",
#             "Phone": "(5) 555-4729",
#             "Fax": "(5) 555-3745"
#         },
#         "ANTON": {
#             "CompanyName": "Antonio Moreno Taquer\u00eda",
#             "ContactName": "Antonio Moreno",
#             "ContactTitle": "Owner",
#             "Address": "Mataderos  2312",
#             "City": "M\u00e9xico D.F.",
#             "Region": "Central America",
#             "PostalCode": "05023",
#             "Country": "Mexico",
#             "Phone": "(5) 555-3932",
#             "Fax": ""
#         },
#     ...


# In the solution, use the built-in csv module and the json package. The tests run several test cases to validate the solution.


# csv documentation: https://docs.python.org/3/library/csv.html

# json documentation: https://docs.python.org/3/library/json.html


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