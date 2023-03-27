# Exercise No. 37


**Note**: This exercise requires basic knowledge of SQL.

**sqlite3 documentation**: https://docs.python.org/3/library/sqlite3.html

Using the *sqlite3* built-in package to manage SQLite databases, a database called *app.db* was created. A table named *category* was also created in this database and several records were inserted:
```

import sqlite3
    
    
conn = sqlite3.connect('apps.db')
cur = conn.cursor()
    
cur.execute('''DROP TABLE IF EXISTS category''')
conn.commit()
    
cur.execute('''CREATE TABLE category (
    category_id   INTEGER,
    category_name TEXT    NOT NULL,
    PRIMARY KEY (category_id));''')
    
cur.execute("INSERT INTO category (category_name) VALUES ('technology')")
cur.execute("INSERT INTO category (category_name) VALUES ('e-commerce')")
cur.execute("INSERT INTO category (category_name) VALUES ('gaming')")
    
conn.commit()
conn.close()
```

For a record with *category_id = 2*, modify the value of *category_name* to `'online shop'`. Then commit the changes and display all the rows of the *category* table as shown below.


#### Expected result:
    (1, 'technology')
    (2, 'online shop')
    (3, 'gaming')


