# Exercise No. 82


The *Matrix* class has been implemented.

Add a method called `add_column()` to the *Matrix* class that allows to add a column to the matrix. The method takes two additional arguments:
-   *column* - the column we want to add to the matrix (list)
-   *index* - the index at which to add the matrix column; default *None* -> adds a column to the end of the matrix

Before the method adds a column to the matrix, some basic validation must be performed. Validation steps:
-   Check if the *column* is an instance of the *list* class. If not, raise the *TypeError* error with the appropriate message (choose the message freely, so that it explains the nature of the error).
-   Check if the *column* items are instances of the *int* or *float* type. If not, raise the *TypeError* error with the appropriate message (choose the message freely, so that it explains the nature of the error).
-   Check if the number of items in the *column* matches the number of rows in the matrix. If not, raise the *ValueError* error with the appropriate message (choose the message freely, so that it explains the nature of the error).


#### Example:


    [IN]: m = Matrix([[3, 1, 6], [5, 2, 6], [0, 4, 2]])
    [IN]: m.add_column([1, 2, 3])
    [IN]: m
    [OUT]: [[3, 1, 6, 1], [5, 2, 6, 2], [0, 4, 2, 3]]


#### Example:


    [IN]: m = Matrix([[3, 1, 6], [5, 2, 6], [0, 4, 2]])
    [IN]: m.add_column([1, 2, 3], 0)
    [IN]: m
    [OUT]: [[1, 3, 1, 6], [2, 5, 2, 6], [3, 0, 4, 2]]


You just need to implement the `add_column()` method. The tests run several test cases to validate the solution.