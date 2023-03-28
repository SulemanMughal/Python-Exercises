# Exercise No. 67

Class inheritance. Consider the built-in *dict* class. We can add *key: value* pairs to the dictionary, for example:


    dict[key] = value


For this purpose, the descriptor `dict.__setitem__()` is called. Equivalently we have:


    dict.__setitem__(key, value)


Inheriting from the *dict* class create a class named *IntDict* that allows you to add only pairs to the dictionary whose value is an *int* object. Raise a *TypeError* with the message otherwise:

`'The value must be an integer.'`


#### Example:


    [IN]: integers = IntDict()
    [IN]: integers['one'] = 1
    [IN]: print(integers)
    [OUT]: {'one': 1, 'two': 2}


#### Example:


    [IN]: integers['one'] = 'uno'
    [OUT]: TypeError: The value must be an integer.


You only need to implement the *IntDict* class. The tests run several test cases to validate the solution.