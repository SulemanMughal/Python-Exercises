# The Stack class has been implemented.

# Implement a function called transfer() that moves all the elements of the first stack to the second stack, so that the item at the top of the first stack is the first item to be inserted into the second stack.

# The transfer() function takes two arguments:

#     stack_1 - the first stack to transfer items from

#     stack_2 - second stack to transfer items to

# and return the given stacks.


# Example:


#     s1 = Stack()
#     s1.push('python')
#     s1.push('java')
#     s1.push('c++')
     
#     s2 = Stack()
#     s2.push('sql')
     
#     s1, s2 = transfer(s1, s2)

#     [IN]: len(s1), len(s2)
#     [OUT]: (0, 4)
     
#     [IN]: s2.pop()
#     [OUT]: 'python'
     
#     [IN]: s2.pop()
#     [OUT]: 'java'


# You just need to implement the transfer() function. 



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
    
    
def transfer(stack_1, stack_2):
    while not stack_1.is_empty():
        stack_2.push(stack_1.pop())
    return stack_1, stack_2