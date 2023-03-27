# The Matrix class has been implemented.

# One of the basic matrix operations is multiplication. Without matrix multiplication, it is impossible to implement, for example, neural networks. Here you need to pay special attention because matrix multiplication is slightly different from operations such as addition or subtraction.

# Before we proceed to implementing matrix multiplication in terms of linear algebra, we will implement a method called multiply_elementwise(), which performs the matrix element-by-element multiplication.

# If the user wants to multiply the matrix by an object of a type other than the Matrix, raise a TypeError with the appropriate message.

# Obviously, the matrices must be of the same size. If the matrices thus multiplied are of different sizes raise the ValueError with the appropriate message.


# Example:


#     [IN]: m1 = Matrix([[2, -1, 5], [9, 4, 5], [5, 2, -1]])
#     [IN]: m2 = Matrix([[-1, 0, 4], [7, 2, -3], [9, 4, -1]])
#     [IN]: m1.multply_elementwise(m2)
#     [OUT]: [[-2, 0, 20], [63, 8, -15], [45, 8, 1]]


# You just need to implement the multiply_elementwise() method. 


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
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(
                'Cannot compare an object that is not a matrix.'
            )
        return self.array == other.array
    
    def __ne__(self, other):
        return not self == other
    
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(
                'Cannot add object that is not a matrix.'
            )
    
        if self.size != other.size:
            raise ValueError(
                'The matrices must be of the same size.'
            )
    
        array = [
            [
                self.array[i][j] + other.array[i][j]
                for j in range(self.n_cols)
            ]
            for i in range(self.n_rows)
        ]
        return Matrix(array)
    
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(
                'Cannot subtract object that is not a matrix.'
            )
    
        if self.size != other.size:
            raise ValueError(
                'The matrices must be of the same size.'
            )
    
        array = [
            [
                self.array[i][j] - other.array[i][j]
                for j in range(self.n_cols)
            ]
            for i in range(self.n_rows)
        ]
        return Matrix(array)
    
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
    
    def identity(self):
        if not self.is_square_matrix:
            return None
        array = [
            [
                1 if row == col else 0
                for row in range(self.n_rows)
            ]
            for col in range(self.n_cols)
        ]
        return Matrix(array)
    
    def add_row(self, row, index=None):
        if not isinstance(row, list):
            raise TypeError('The matrix row must be a list.')
    
        for number in row:
            if not type(number) in (int, float):
                raise TypeError(
                    'Row values must be int or float.'
                )
    
        if len(row) != self.n_cols:
            raise ValueError(
                'The row must be the same length as the number '
                'of columns in the matrix.'
            )
    
        if index is None:
            self.array.append(row)
        else:
            self.array = (
                self.array[0:index] + [row] + self.array[index:]
            )
    
    def add_column(self, column, index=None):
        if not isinstance(column, list):
            raise TypeError('The matrix column must be a list.')
    
        for number in column:
            if not type(number) in (int, float):
                raise TypeError(
                    'Column values must be int or float.'
                )
    
        if len(column) != self.n_rows:
            raise ValueError(
                'The column must be the same length as the number '
                'of rows in the matrix.'
            )
    
        if index is None:
            self.array = [
                self.array[idx] + [column[idx]]
                for idx in range(self.n_rows)
            ]
        else:
            self.array = [
                self.array[idx][0:index]
                + [column[idx]]
                + self.array[idx][index:]
                for idx in range(self.n_rows)
            ]
    
    def transpose(self):
        array = [
            [row[idx] for row in self.array]
            for idx in range(self.n_cols)
        ]
        return Matrix(array)
    
    def multiply_elementwise(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(
                'Cannot multiply object that is not a matrix.'
            )
    
        if self.size != other.size:
            raise ValueError(
                'The matrices must be of the same size.'
            )
    
        array = [
            [
                self.array[i][j] * other.array[i][j]
                for j in range(self.n_cols)
            ]
            for i in range(self.n_rows)
        ]
        return Matrix(array)