# Exercise No. 85


The *Matrix* class has been implemented.

One of the basic matrix operations is addition. Add the `__add__()` method to the *Matrix* implementation that allows to add matrices (element by element).

If the user wants to add an object of a type other than the *Matrix* instance, raise a *TypeError* with the appropriate message.

Obviously, the matrices must be of the same size. If matrices are of different sizes raise the *ValueError* with the appropriate message.

Add the implementation of the `__add__()` method right after the `__ne__()` method.


#### Example:


    [IN]: m1 = Matrix([[1, 4], [5, 2]])
    [IN]: m2 = Matrix([[2, 5], [1, 3]])
    [IN]: m1 + m2
    [OUT]: [[3, 9], [6, 5]]
     
    [IN]: m1.__add__(m2)
    [OUT]: [[3, 9], [6, 5]]


#### Example:


    [IN]: m1 = Matrix([[1, 4, -3], [5, 2, -1]])
    [IN]: m2 = Matrix([[2, -3, 5], [-2, 1, 3]])
    [IN]: m1 + m2
    [OUT]: [[3, 1, 2], [3, 3, 2]]


You just need to add the `__add__()` method. The tests run several test cases to validate the solution.


