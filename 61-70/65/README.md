# Exercise No. 65

Class inheritance. Consider a built-in *list* class. One of the methods of this class is the `append()` method, which appends an item at the end of the list:


    >>> help(list.append)
     
    Help on method_descriptor:
    append(self, object, /)
        Append object to the end of the list.


An element can be, for example, an object of class *int*, *float*, *str*, *bool* or *NoneType*.

By inheriting from a list class create a class named *IntList* that allows you to append only *int* objects with the `append()` method. If you try to append an object of a different type raise a *TypeError* with the message:

`'The value must be an integer.'`


#### Example:


    [IN]: integers = IntList()
    [IN]: integers.append(3)
    [IN]: integers.append(40)
    [IN]: print(integers)
    [OUT]: [3, 40]


#### Example:


    [IN]: integers.append('sql')
    [OUT]: TypeError: The value must be an integer.


You only need to implement the *IntList* class. The tests run several test cases to validate the solution.