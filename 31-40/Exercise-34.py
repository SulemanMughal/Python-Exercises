# Note: This exercise requires basic knowledge of SQL.

# sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html


# Using sqlite3 to manage SQLite databases, create a database named app.db.

# The following SQL code creates a table named customer with columns: customer_id, first_name, last_name, and email.


#     CREATE TABLE IF NOT EXISTS customer (
#         customer_id INTEGER PRIMARY KEY,
#         first_name  TEXT,
#         last_name   TEXT,
#         email       TEXT
#     )


# Using the above SQL code create the customer table in the app.db database. Then insert the following records into the customer table using the executescript() method:


#     ('John', 'Smith', 'john.smith@esmartdata.org')
#     ('Joe', 'Doe', 'joe.doe@esmartdata.org')
#     ('Mike', 'Smith', 'mike.smith@esmartdata.org')


# Commit the changes and close the database connection. 

import sqlite3
    
    
conn = sqlite3.connect('app.db')
cur = conn.cursor()
    
cur.execute('''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)''')
    
cur.executescript('''INSERT INTO customer (first_name, last_name, email)
VALUES ('John', 'Smith', 'john.smith@esmartdata.org');
    
INSERT INTO customer (first_name, last_name, email)
VALUES ('Joe', 'Doe', 'joe.doe@esmartdata.org');
    
INSERT INTO customer (first_name, last_name, email)
VALUES ('Mike', 'Smith', 'mike.smith@esmartdata.org');''')
    
conn.commit()
conn.close()