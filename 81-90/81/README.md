# Exercise No. 81

The *Matrix* class has been implemented.

Add a method called `add_row()` to the *Matrix* class that allows to add a row to the matrix. The method takes two additional arguments:
-   *row* - the row we want to add to the matrix (list)
-   *index* - the index at which to add the matrix row; default *None* -> adds a row to the end of the matrix

Before the method adds a row to the matrix, some basic validation must be performed. Validation steps:
-   Check if the row is an instance of the *list* class. If not, raise the *TypeError* error with the appropriate message (choose the message freely, so that it explains the nature of the error).
-   Check if the *row* items are instances of the *int* or *float* type. If not, raise the *TypeError* error with the appropriate message (choose the message freely, so that it explains the nature of the error).
-   Check if the number of items in the *row* matches the number of columns in the matrix. If not, raise the *ValueError* error with the appropriate message (choose the message freely, so that it explains the nature of the error).


#### Example:


    [IN]: m = Matrix([[3, 1, 6], [5, 2, 6], [5, 2, 6]])
    [IN]: m.add_row([5, 7, 3])
    [IN]: m
    [OUT]: [[3, 1, 6], [5, 2, 6], [0, 4, 2], [5, 7, 3]]


#### Example:


    [IN]: m = Matrix([[3, 1, 6], [5, 2, 6], [0, 4, 2]])
    [IN]: m.add_row([5, 7, 3], 2)
    [IN]: m
    [OUT]: [[3, 1, 6], [5, 2, 6], [5, 7, 3], [0, 4, 2]]


You only need to implement the `add_row()` method. The tests run several test cases to validate the solution.