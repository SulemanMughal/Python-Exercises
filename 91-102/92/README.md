# Exercise No. 92

The *Stack* class has been implemented.

Add a method called `is_empty()` to the *Stack* class that checks if the stack is empty. If the stack is empty, the method should return the boolean value *True*, on the contrary *False*. Also modify the pop() method using `is_empty()` method in the conditional statement.


#### Example:


    [IN]: techs = Stack()
    [IN]: techs.push('python')
    [IN]: len(techs)
    [OUT]: 1
     
    [IN]: techs.is_empty()
    [OUT]: False
     
    [IN]: techs.pop()
    [OUT]: 'python'
     
    [IN]: techs.is_empty()
    [OUT]: True


The tests run several test cases to validate the solution.