
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