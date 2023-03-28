# Exercise No. 83


The *Matrix* class has been implemented.

Add the `__eq__()` special method to the *Matrix* class, which allows you to compare *Matrix* instances. Two instances are equal when they have the same elements. If the user passes an object of a class other than the *Matrix* for comparison, raise the *TypeError* with an appropriate message (choose the message freely, so that it explains the nature of the error).

Add the implementation of the `__eq__()` method right after the `__repr__()` method.


#### Example:


    [IN]: m1 = Matrix([[1, 4], [5, 2]])
    [IN]: m2 = Matrix([[1, 4], [5, 2]])
    [IN]: m1 == m2
    [OUT]: True
     
    [IN]: m1.__eq__(m2)
    [OUT]: True


#### Example:


    [IN]: m1 = Matrix([[1, 4], [5, 2]])
    [IN]: m1 == [1, 4]
    [OUT]: TypeError: Cannot compare an object that is not a matrix.


You just need to add the `__eq__()` method. The tests run several test cases to validate the solution.