# The Matrix class has been implemented.

# Add a method called zero() to the Matrix class that returns a zero matrix of the same size (a matrix filled with zeros).


# Example:


#     [IN]: m = Matrix([[3, 1, 6], [5, 2, 6], [5, 2, 6]])
#     [IN]: m.zero()
#     [OUT]: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Example:


#     [IN]: m = Matrix([[3, 1, 6]])
#     [IN]: m.zero()
#     [OUT]: [[0, 0, 0]]


# You only need to implement the zero() method.



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
    
    def zero(self):
        array = [
            [0 for _ in range(self.n_cols)]
            for _ in range(self.n_rows)
        ]
        return Matrix(array)