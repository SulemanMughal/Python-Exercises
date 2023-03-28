# Exercise No. 87

The *Matrix* class has been implemented.

One of the basic matrix operations is transposition. A transposed matrix is created by replacing its rows with columns and columns with rows.

Add a method named `transpose()` to the implementation of the *Matrix* class that allows you to create a transposed matrix.


#### Example:


    [IN]: m = Matrix([[2, 5, 4], [1, 3, 2]])
    [IN]: m.transpose()
    [OUT]: [[2, 1], [5, 3], [4, 2]]


#### Example:


    [IN]: m = Matrix([[2, -1, 5], [9, 4, 5], [5, 2, -1]])
    [IN]: m.transpose()
    [OUT]: [[2, 9, 5], [-1, 4, 2], [5, 5, -1]]


You just need to add the `transpose()` method. The tests run several test cases to validate the solution.