# Exercise No. 41


**Note**: This exercise requires basic knowledge of SQL.

**sqlite3 documentation**: https://docs.python.org/3/library/sqlite3.html

**csv documentation**: https://docs.python.org/3/library/csv.html


The file *Product.csv* (utf-8 coding) containing data about products in a certain warehouse is attached to the exercise. In this exercise, you will create a SQLite database (named *store.db*) with a table named *Product* and the data contained in the *Product.csv* file.

Extract the names of the *Product* table columns from the first line of the *Products.csv* file:
    
    "Id",
    "ProductName",
    "SupplierId",
    "CategoryId",
    "QuantityPerUnit",
    "UnitPrice",
    "UnitsInStock",
    "UnitsOnOrder",
    "ReorderLevel",
    "Discontinued",


*Product* table constraints are included in the *product_constraints* list:

    product_constraints = [
        'INTEGER PRIMARY KEY',
        'TEXT NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
        'TEXT NOT NULL',
        'REAL NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
        'INTEGER NOT NULL',
    ]


Use the `generate_sql()` function from the previous exercise to generate the SQL that creates the *Product* table:
```
def generate_sql(table_name, col_names, constraints):
    cols = [
        " ".join((col, constraint)).strip()
        for col, constraint in zip(col_names, constraints)
    ]
    return f'CREATE TABLE {table_name} (' + ', '.join(cols) + ')'
```

Then create the *Product* table and insert data from *Product.csv*. In response, create a query to *store.db* that extracts the number of records in the *Product* table and print it to the console.


In the solution, use the built-in *sqlite3* package. The built-in *csv* module may be helpful to work with the csv file.


#### Expected result:
    77