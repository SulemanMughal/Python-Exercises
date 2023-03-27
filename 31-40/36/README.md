# Exercise No. 36


**Note**: This exercise requires basic knowledge of SQL.

**sqlite3 documentation**: https://docs.python.org/3/library/sqlite3.html


Using *sqlite3* to manage SQLite databases, create a database named *app.db*.

Then create a table named *category* with the following columns (and constraints):

-   *category_id* - INTEGER PRIMARY KEY
-   *category_name* - TEXT NOT NULL

Then insert the following records into the *category* table using the following SQL code and commit the changes.

```
INSERT INTO category (category_name) VALUES ('technology');
INSERT INTO category (category_name) VALUES ('e-commerce')
INSERT INTO category (category_name) VALUES ('gaming')
```


Create a query to the *app.db* database and select all rows from the *category* table. Assign them to a list named *categories*. In response, print the *categories* list to the console.

Close the database connection. The tests run several test cases to validate the solution.


#### Expected result:
    [(1, 'technology'), (2, 'e-commerce'), (3, 'gaming')]