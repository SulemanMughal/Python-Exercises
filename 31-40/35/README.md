# Exercise No. 35


**Note**: This exercise requires basic knowledge of SQL.

**sqlite3 documentation**: https://docs.python.org/3/library/sqlite3.html

Using the *sqlite3* built-in package to manage SQLite databases, a database called *app.db* was created. A table named *customer* was also created in this database and several records were inserted:

```
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
```


In the designated place, create a query that will extract the number of all records from the *customer* table and print it to the console.


#### Expected result:
    3