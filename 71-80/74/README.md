# Exercise No. 74


In this exercise, we will use the basics of linear algebra.


Implement a class called *Matrix* that will provide an interface for matrices. In this exercise, we will only implement two special methods:

-   the special method `__init__()`

-   the special method `__repr__()`

If you don't know what the above special methods are for, take a look at the object-oriented programming course.

The matrix will be stored using a nested list (instance attribute named *array* - recommended name). The `__repr__()` method will return the representation of the matrix as a nested list (see below for examples).

#### Examples:


    [IN]: Matrix([[5]])
    [OUT]: [[5]]
     
    [IN]: Matrix([[5], [6]])
    [OUT]: [[5], [6]]
     
    [IN]: Matrix([[5, 2], [0, 6]])
    [OUT]: [[5, 2], [0, 6]]
     
    [IN]: Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    [OUT]: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


When creating a *Matrix* instance, we pass a nested list and assign it to the array instance attribute. Let's add some level of validation. A user of the *Matrix* class may by mistake pass other objects from which we are unable to create a matrix.

What can go wrong? For example, a user can pass an object of a different type:


    Matrix({5, 4})


The user can pass a list that is not nested:


    Matrix([5, 3, 6])


The user can pass a list that is nested but contains no values:


    Matrix([[], []])


The user can pass a different number of elements for the columns:


    Matrix([[5], [6, 8, 2]])


The user can pass a nested list that consists of elements other than *int* or *float*:


    Matrix([['python'], ['sql']])


In the `__init__()` method, perform the validation before setting an instance attribute (*array*):

-   check if argument is an instance of class *list*, if not raise *TypeError* with message:

        'To create a matrix you need to pass a nested list of values.'

-   check that the list contains any element, if not set the value of the *array* instance attribute to an empty list `[]`
-   check if all the elements of the list are list, if not raise a *TypeError* with the message: 

        'Each element of the array (nested list) must be a list.'

-   check if columns have the same number of elements, if not raise *TypeError* with message:

        'All columns must be the same length.'

-   check if all nested list items are int or float, if not raise *TypeError* with message:

        'The values must be of type int or float.'
