
import csv
import sqlite3
    
    
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
    
    
def generate_sql(table_name, col_names, constraints):
    cols = [
        " ".join((col, constraint)).strip()
        for col, constraint in zip(col_names, constraints)
    ]
    return f'CREATE TABLE {table_name} (' + ', '.join(cols) + ')'
    
    
# Read csv file
with open('Product.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = tuple(reader)
    
# Create SQL code
sql_create_table = generate_sql(
    'Product', columns, product_constraints
)
    
# Create a DB connection
conn = sqlite3.connect('store.db')
cur = conn.cursor()
    
# Create Product table
cur.execute(sql_create_table)
cur.executemany(
    '''INSERT INTO Product VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    rows,
)
conn.commit()
    
# Select number of rows
cur.execute('''SELECT COUNT(*) FROM Product''')
total_rows = cur.fetchall()[0][0]
print(total_rows)
    
conn.close()