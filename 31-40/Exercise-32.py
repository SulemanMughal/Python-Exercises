# Note: This exercise requires basic knowledge of SQL.

# sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html


# Using sqlite3 package to manage SQLite databases, create a database named app.db.

# The following SQL code creates a table named customer with columns: customer_id, first_name, last_name, and email.


#     CREATE TABLE IF NOT EXISTS customer (
#         customer_id INTEGER PRIMARY KEY,
#         first_name  TEXT,
#         last_name   TEXT,
#         email       TEXT
#     )


# Using the above SQL code create the customer table in the app.db database. Then insert the following record into the customer table:


#     ('John', 'Smith', 'john.smith@esmartdata.org')


# Commit the changes and close the database connection. The tests run several test cases to validate the solution.


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
    
# Insert a row
cur.execute('''INSERT INTO customer (first_name, last_name, email)
VALUES ('John', 'Smith', 'john.smith@esmartdata.org')''')
    
# Commit changes
conn.commit()
    
# Close connection
conn.close()