# The Stack class has been implemented.

# Implement a function called is_palindrome() that checks if the text is a palindrome. A palindrome is an expression that sounds the same way read left to right and right to left. For example, the following expressions are a palindrome:

#     'civic'

#     'kayak'

#     'level'

#     'pip'

# The function returns True if the expression is a palindrome, on the contrary, False. The function takes one argument.

# When implementing is_palindrome() function, think about how you can solve this problem using the stack. For this purpose, use the Stack class.

# Example:


#     [IN]: is_palindrome('kajak')
#     [OUT]: True
     
#     [IN]: is_palindrome('kajaki')
#     [OUT]: False


# You just need to implement the is_palindrome() function. 

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
    
    
def is_palindrome(string):
    stack = Stack()
    is_palindrome_flag = True
    
    for char in string:
        stack.push(char)
    
    for char in string:
        if not char == stack.pop():
            is_palindrome_flag = False
    
    return is_palindrome_flag