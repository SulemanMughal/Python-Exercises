# Exercise No. 75

The Matrix class has been implemented.

Please note that the following condition:


    if not all(
        isinstance(number, (int, float))
        for row in array
        for number in row
    ):
        raise TypeError('The values must be of type int or float.')


checks if the elements of a matrix are instances of the *int* or *float* type. However, we must remember that the *bool* class in Python is a built-in class that inherits from the *int* class and the following:


    isinstance(True, int)


returns *True*. Thus, with our implementation, we are able to create a matrix:


    [IN]: Matrix([[True, False], [True, True]])
    [OUT]: [[True, False], [True, True]]


Modify the implementation of the *Matrix* class to eliminate this behavior.


