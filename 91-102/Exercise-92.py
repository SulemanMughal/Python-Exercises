# The Stack class has been implemented.

# Add a method called is_empty() to the Stack class that checks if the stack is empty. If the stack is empty, the method should return the boolean value True, on the contrary False. Also modify the pop() method using is_empty() method in the conditional statement.


# Example:


#     [IN]: techs = Stack()
#     [IN]: techs.push('python')
#     [IN]: len(techs)
#     [OUT]: 1
     
#     [IN]: techs.is_empty()
#     [OUT]: False
     
#     [IN]: techs.pop()
#     [OUT]: 'python'
     
#     [IN]: techs.is_empty()
#     [OUT]: True


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