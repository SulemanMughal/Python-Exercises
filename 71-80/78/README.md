# Exercise No. 78

The *Matrix* class has been implemented.

Add a read-only property to the *Matrix* class named *is_square_matrix*, which returns *True* if the matrix is a square matrix, otherwise *False*.


**Reminder**: A matrix is a square matrix when the number of rows and the number of columns are equal.


#### Example:


    [IN]: m = Matrix([[3, 1, 6], [5, 2, 6]])
    [IN]: m.is_square_matrix
    [OUT]: False


#### Example:


    [IN]: Matrix([[3, 1, 6], [5, 2, 6], [5, 2, 6]])
    [IN]: m.is_square_matrix
    [OUT]: True


You only need to complete the implementation of the *Matrix* class. The tests run several test cases to validate the solution.