# Exercise No. 89

The *Matrix* class has been implemented.

One of the basic matrix operations is multiplication. Without matrix multiplication, it is impossible to implement, for example, neural networks. Here you need to pay special attention because matrix multiplication is slightly different from operations such as addition or subtraction.

Before we proceed to the implementation of the `__mul__()` method, we will add class method called `dot()`. For this we can use the *@classmethod* decorator.

We can treat the rows and columns of the matrix separately as vectors and calculate their dot product.

For example, the dot product of vectors `dot([-1, 4, 5], [-4, 0, 1])` is equal to 9, because:


    dot([-1, 4, 5], [-4, 0, 1]) = (-1) * (-4) + 4 * 0 + 5 * 1 = 4 + 0 + 5 = 9


The `dot()` method takes two additional arguments:
-   *row* - row of the matrix (list)
-   *column* - column of the matrix (list)


If the user wants to pass an object other than the *list* type to the `dot()` method, raise a *TypeError* with the appropriate message.

In this case, we don't validate the length of the *row* and *column* lists. We assume that the user is passing the correct length of the lists. We will use the `dot()` method in the next exercise to implement matrix multiplication.


#### Example:


    [IN]: Matrix.dot([-1, 4, 5], [-4, 0, 1])
    [OUT]: 9


#### Example:


    [IN]: Matrix.dot([-1, -3], [10, -2])
    [OUT]: -4


You just need to implement the `dot()` method. The tests run several test cases to validate the solution.