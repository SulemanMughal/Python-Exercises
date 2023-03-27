# The Stack class has been implemented.

# Add a method called top() to the Stack class that reads the item at the top of the stack (without removing the item from the stack). If the stack is empty raise the EmptyStackError with the message: 'The stack is empty.'


# Example:


#     [IN]: techs = Stack()
#     [IN]: techs.push('python')
#     [IN]: techs.push('django')
#     [IN]: techs.top()
#     [OUT]: 'django'
     
#     [IN]: len(techs)
#     [OUT]: 2
     
#     [IN]: techs.pop()
#     [OUT]: 'django'
     
#     [IN]: techs.pop()
#     [OUT]: 'python'
     
#     [IN]: techs.top()
#     [OUT]: EmptyStackError: The stack is empty.


# You just need to implement the top() method of the Stack class. 


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