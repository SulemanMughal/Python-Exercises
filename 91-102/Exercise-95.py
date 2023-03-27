# # The Stack class has been implemented.

# Implement a function called is_valid_expression() that checks if the expression (in the form of a str object) is valid for the number of open and closed parentheses. In this exercise, we take into account the brackets like: (), [], {}.

# Examples of valid expressions:

#     '(3 + x) * 2'

#     'for i in range(size):'

# Examples of invalid expressions:

#     '(3 + x] * 2'

#     'for i in range(size:'

# The function returns True if the expression is valid, on the contrary, False. The function takes one argument.

# When implementing is_valid_expression() function, think about how you can solve this problem using the stack. For this purpose, use the Stack class.


# Example:


#     [IN]: is_valid_expression('(3 + x) * 2')
#     [OUT]: True
     
#     [IN]: is_valid_expression('2 - [(3 + x) * 2)')
#     [OUT]: False


# You just need to implement the is_valid_expression() function.



class EmptyStackError(Exception):
    pass
    
    
class Stack:
    """The simplest stack."""
    
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()
    
    def is_empty(self):
        return len(self._data) == 0
    
    def top(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data[-1]
    
    
def is_valid_expression(expression):
    left_side = '([{'
    right_side = ')]}'
    
    stack = Stack()
    
    for char in expression:
        if char in left_side:
            stack.push(char)
        elif char in right_side:
            if stack.is_empty():
                return False
            if right_side.index(char) != left_side.index(stack.pop()):
                return False
    return stack.is_empty()