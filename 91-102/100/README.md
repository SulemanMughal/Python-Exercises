# Exercise No. 100


In computer science, a **queue** is a collection of objects that are maintained in a sequence and can be modified by the addition of objects at one end of the sequence and the removal of objects from the other end of the sequence.

The operation of adding an element to the end of the sequence is known as *enqueue*, and the operation of removing an element from the front is known as *dequeue*. The operations of a queue make it a *first-in-first-out (FIFO)* data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed.

For example, a line of people waiting at the checkout in a store is a queue. Queues are used by many computing devices.

Implement a class named *Queue* that will represent the queue. Required methods that we must implement:

-   `enqueue(item)` -> put an item at the end of the queue

-   `dequeue()` -> delete and return item from the front of the queue; if the queue is empty raise *IndexError* with the message: 

    `'The queue is empty.'`

In addition to the methods described above, add implementations of two special methods:

-   `__init__()` -> set a protected attribute named _data that stores the queue objects as a list

-   `__len__()` -> define the built-in function len() -> number of stack elements.


#### Example:


    [IN]: que = Queue()
    [IN]: que.enqueue('529')
    [IN]: que.enqueue('512')
    [IN]: len(que)
    [OUT]: 2
     
    [IN]: que.enqueue('844')
    [IN]: que.dequeue()
    [OUT]: '529'
     
    [IN]: len(que)
    [OUT]: 2


You only need to implement the *Queue* class. The tests run several test cases to validate the solution.