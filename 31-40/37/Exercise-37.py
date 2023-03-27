
import sqlite3
    
    
conn = sqlite3.connect('app.db')
cur = conn.cursor()
    
cur.execute('''CREATE TABLE category (
    category_id   INTEGER,
    category_name TEXT    NOT NULL,
    PRIMARY KEY (category_id)
)''')
    
cur.execute("INSERT INTO category (category_name) VALUES ('technology')")
cur.execute("INSERT INTO category (category_name) VALUES ('e-commerce')")
cur.execute("INSERT INTO category (category_name) VALUES ('gaming')")
conn.commit()
    
cur.execute(
    "UPDATE category SET category_name = 'online shop' "
    "WHERE category_id = 2"
)
conn.commit()
    
cur.execute('''SELECT * FROM category''')
rows = cur.fetchall()
    
for row in rows:
    print(row)
    
conn.close()