# Exercise No. 91


In computer science, a *stack* is a data structure used to store a collection of objects. Individual items can be added and stored in a stack using a push operation. Objects can be retrieved using a *pop* operation, which removes an item from the stack. A stack contains objects that are inserted and removed according to the LIFO (last-in, first-out) principle. The user can insert items into the stack at any time, but can only access or delete the last inserted item that remains on the so-called top of the stack.

We can imagine a stack, for example, as a stack of books on a desk. New books are added to the top of the stack. If we want to take a book, we also take it from the top of the stack.

Lots of algorithms use stacks. Web browsers can store the addresses of recently visited sites in a stack. Each time a user visits a new site, that site's address is added to the stack. The browser then allows the user to go back to previously visited sites using the 'Back' button.

Implement a class named *Stack* that represents the stack (abstract data type). Required methods that we must implement:
-   `push(item)` -> adding an item to the top of the stack
-   `pop()` -> delete and return an item from the top of the stack; if the stack is empty raise an error named EmptyStackError with the message: `'The stack is empty.'`



Add an error named *EmptyStackError* using inheritance from the built-in *Exception* class.

In addition to the methods described above, add implementations of two special methods:

-   `__init__()` -> set a protected attribute named `_data` that stores the stack items as a list

-   `__len__()` -> define the built-in function `len()` -> number of stack elements


#### Example:


    [IN]: techs = Stack()
    [IN]: techs.push('python')
    [IN]: techs.push('sql')
    [IN]: len(techs)
    [OUT]: 2
     
    [IN]: techs.pop()
    [OUT]: 'sql'
     
    [IN]: len(techs)
    [OUT]: 1
     
    [IN]: techs.pop()
    [OUT]: 'python'
     
    [IN]: techs.pop()
    [OUT]: EmptyStackError: The stack is empty.


You just need to implement the *Stack* class. The tests run several test cases to validate the solution.