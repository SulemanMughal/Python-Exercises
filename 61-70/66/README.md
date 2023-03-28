# Exercise No. 66

Class inheritance. Consider a built-in *list* class. One of the methods of this class is the `append()` method, which appends an item at the end of the list:


    >>> help(list.append)
     
    Help on method_descriptor:
    append(self, object, /)
        Append object to the end of the list.


An element can be, for example, an object of class *int*, *float*, *str*, *bool* or *NoneType*.

Suppose we have a problem to solve that requires us to use a list, and we don't want to let users append items of different types to the list. We would like to limit this operation only for natural numbers. For the purposes of solution we do not consider 0 to be a natural number.

By inheriting from *list* class create a class named *NaturalList* that allows you to append only naural numbers with the `append()` method.

If you try to append an object of a different type raise a *TypeError* with the message:

`'The value must be an integer.'`

Raise the *ValueError* with the message below if you try to add a number that is not a natural number:

`'The value must be a natural number.'`


#### Example:


    [IN]: integers = IntList()
    [IN]: integers.append(3)
    [IN]: print(integers)
    [OUT]: [3]


#### Example:


    [IN]: integers.append('sql')
    [OUT]: TypeError: The value must be an integer.


#### Example:


    [IN]: integers.append(-4)
    [OUT]: ValueError: The value must be a natural number.


You only need to implement the *NaturalList* class. The tests run several test cases to validate the solution.