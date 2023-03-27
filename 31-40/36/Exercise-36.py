
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
categories = cur.execute('''SELECT * FROM category''').fetchall()
print(categories)
    
conn.close()