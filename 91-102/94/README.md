# Exercise No. 94

The *Stack* class has been implemented.

Add a method called `top()` to the *Stack* class that reads the item at the top of the stack (without removing the item from the stack). If the stack is empty raise the *EmptyStackError* with the message: 'The stack is empty.'


#### Example:


    [IN]: techs = Stack()
    [IN]: techs.push('python')
    [IN]: techs.push('django')
    [IN]: techs.top()
    [OUT]: 'django'
     
    [IN]: len(techs)
    [OUT]: 2
     
    [IN]: techs.pop()
    [OUT]: 'django'
     
    [IN]: techs.pop()
    [OUT]: 'python'
     
    [IN]: techs.top()
    [OUT]: EmptyStackError: The stack is empty.


You just need to implement the `top()` method of the *Stack* class. The tests run several test cases to validate the solution.