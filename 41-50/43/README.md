# Exercise No. 43


The file *Customer.csv* (utf-8 coding) containing data about the customers of a certain application is attached to the exercise.

Convert the data from the *Customer.csv* file to a dictionary named *data_dict*. The *data_dict* dictionary keys are to be the `'Id'` values from the *Customer.csv* file, and the values for these keys will be dictionaries of the form: *ColumnName*: Value of data from *Customer.csv* file. The first few elements of the dictionary:

    {'ALFKI': {'CompanyName': 'Alfreds Futterkiste', 'ContactName' ...
    {'ANATR', {'CompanyName': 'Ana Trujillo Emparedados y helados' ...
    {'ANTON', {'CompanyName': 'Antonio Moreno Taquería', 'ContactName' ...
    ...


In response, print to the console the value for the `'BOLID'` key of the *data_dict* dictionary.


In the solution, use the built-in *csv* module.


**csv documentation**: https://docs.python.org/3/library/csv.html


#### Expected result:

    {'CompanyName': 'Bólido Comidas preparadas', 'ContactName': 'Martín Sommer', 'ContactTitle': 'Owner', 'Address': 'C/ Araquil, 67', 'City': 'Madrid', 'Region': 'Southern Europe', 'PostalCode': '28023', 'Country': 'Spain', 'Phone': '(91) 555 22 82', 'Fax': '(91) 555 91 99'}