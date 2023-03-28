# Exercise No. 88

The *Matrix* class has been implemented.

One of the basic matrix operations is multiplication. Without matrix multiplication, it is impossible to implement, for example, neural networks. Here you need to pay special attention because matrix multiplication is slightly different from operations such as addition or subtraction.

Before we proceed to implementing matrix multiplication in terms of linear algebra, we will implement a method called `multiply_elementwise()`, which performs the matrix element-by-element multiplication.

If the user wants to multiply the matrix by an object of a type other than the *Matrix*, raise a *TypeError* with the appropriate message.

Obviously, the matrices must be of the same size. If the matrices thus multiplied are of different sizes raise the *ValueError* with the appropriate message.


#### Example:


    [IN]: m1 = Matrix([[2, -1, 5], [9, 4, 5], [5, 2, -1]])
    [IN]: m2 = Matrix([[-1, 0, 4], [7, 2, -3], [9, 4, -1]])
    [IN]: m1.multply_elementwise(m2)
    [OUT]: [[-2, 0, 20], [63, 8, -15], [45, 8, 1]]


You just need to implement the `multiply_elementwise()` method. The tests run several test cases to validate the solution.