# The Matrix class has been implemented.

# Add a read-only property to the Matrix class named is_square_matrix, which returns True if the matrix is a square matrix, otherwise False.


# Reminder: A matrix is a square matrix when the number of rows and the number of columns are equal.


# Example:


#     [IN]: m = Matrix([[3, 1, 6], [5, 2, 6]])
#     [IN]: m.is_square_matrix
#     [OUT]: False


# Example:


#     [IN]: Matrix([[3, 1, 6], [5, 2, 6], [5, 2, 6]])
#     [IN]: m.is_square_matrix
#     [OUT]: True


# You only need to complete the implementation of the Matrix class.



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
    
    @property
    def n_rows(self):
        return len(self.array)
    
    @property
    def n_cols(self):
        if len(self.array) == 0:
            return 0
        return len(self.array[0])
    
    @property
    def size(self):
        return self.n_rows, self.n_cols
    
    @property
    def is_square_matrix(self):
        return self.size[0] == self.size[1]