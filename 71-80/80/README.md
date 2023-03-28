# Exercise No. 80

The *Matrix* class has been implemented.

Add a method called `identity()` to the *Matrix* class that returns the identity matrix for square matrix, otherwise *None*.


**Reminder**: The identity matrix of size *n* is the *n × n* square matrix with ones on the main diagonal and zeros elsewhere.


#### Example:


    [IN]: m = Matrix([[3, 1, 6], [5, 2, 6], [5, 2, 6]])
    [IN]: m.identity()
    [OUT]: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


#### Example:


    [IN]: m = Matrix([[3, 1, 6]])
    [IN]: m.identity()
    [OUT]: None


You just need to implement the `identity()` method. The tests run several test cases to validate the solution.