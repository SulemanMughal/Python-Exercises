# Note: This exercise requires basic knowledge of SQL.

# sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html


# Using the sqlite3 built-in package to manage SQLite databases, a database called app.db was created. A table named customer was also created in this database and two records were inserted:


#     import sqlite3
     
     
#     # Create connection
#     conn = sqlite3.connect('app.db')
#     cur = conn.cursor()
     
#     # Create table
#     sql = '''CREATE TABLE IF NOT EXISTS customer (
#         customer_id INTEGER PRIMARY KEY,
#         first_name  TEXT,
#         last_name   TEXT,
#         email       TEXT
#     )'''
#     cur.execute(sql)
     
#     # Insert rows
#     cur.execute('''INSERT INTO customer (first_name, last_name, email)
#     VALUES ('John', 'Smith', 'john.smith@esmartdata.org')''')
#     cur.execute('''INSERT INTO customer (first_name, last_name, email)
#     VALUES ('Mike', 'Doe', 'mike.doe@esmartdata.org')''')
     
#     # Commit changes
#     conn.commit()
     
#     # Close connection
#     conn.close()


# In the designated place, create a query that will extract all records from the customer table and print them to the console.


# Expected result:


#     [(1, 'John', 'Smith', 'john.smith@esmartdata.org'), (2, 'Mike', 'Doe', 'mike.doe@esmartdata.org')]


import sqlite3
    
    
# Create connection
conn = sqlite3.connect('app.db')
cur = conn.cursor()
    
# Create table
sql = '''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)'''
cur.execute(sql)
    
# Insert rows
cur.execute('''INSERT INTO customer (first_name, last_name, email)
VALUES ('John', 'Smith', 'john.smith@esmartdata.org')''')
cur.execute('''INSERT INTO customer (first_name, last_name, email)
VALUES ('Mike', 'Doe', 'mike.doe@esmartdata.org')''')
    
# Make a query
cur.execute('''SELECT * FROM customer''')
result = cur.fetchall()
print(result)
    
# Commit changes
conn.commit()
    
# Close connection
conn.close()