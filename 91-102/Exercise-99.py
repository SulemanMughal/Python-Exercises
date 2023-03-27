# The Stack class has been implemented.

# Add a method called clear() to the Stack class that clears the stack (remove all items in the stack).


# Example:


#     [IN]: techs = Stack()
#     [IN]: techs.push('python')
#     [IN]: techs.push('django')
#     [IN]: len(techs)
#     [OUT]: 2
     
#     [IN]: techs.clear()
#     [IN]: len(techs)
#     [OUT]: 0


# You just need to implement the clear() method of the Stack class. 


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
    
    def clear(self):
        self._data.clear()