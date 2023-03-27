# The Matrix class has been implemented.

# Please note that the following condition:


#     if not all(
#         isinstance(number, (int, float))
#         for row in array
#         for number in row
#     ):
#         raise TypeError('The values must be of type int or float.')


# checks if the elements of a matrix are instances of the int or float type. However, we must remember that the bool class in Python is a built-in class that inherits from the int class and the following:


#     isinstance(True, int)


# returns True. Thus, with our implementation, we are able to create a matrix:


#     [IN]: Matrix([[True, False], [True, True]])
#     [OUT]: [[True, False], [True, True]]


# Modify the implementation of the Matrix class to eliminate this behavior.



class Matrix:
    def __init__(self, array):
    
        if not isinstance(array, list):
            raise TypeError(
                'To create a matrix you need to pass a nested '
                'list of values.'
            )
    
        if len(array) != 0:
            if not all(isinstance(row, list) for row in array):
                raise TypeError(
                    'Each element of the array (nested list) must '
                    'be a list.'
                )
    
            if not all(len(row) for row in array):
                raise TypeError(
                    'Columns must contain at least one item.'
                )
    
            column_length = len(array[0])
    
            if not all(
                len(row) == column_length for row in array
            ):
                raise TypeError(
                    'All columns must be the same length.'
                )
    
            if not all(
                type(number) in (int, float)
                for row in array
                for number in row
            ):
                raise TypeError(
                    'The values must be of type int or float.'
                )
    
            self.array = array
    
        else:
            self.array = []
    
    def __repr__(self):
        return str(self.array)