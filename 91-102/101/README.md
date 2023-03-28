# Exercise No. 101

The *Queue* class has been implemented.

Add two methods to the *Queue* class:

-   a method called `is_empty()` which checks if the queue is empty; the method returns *True* or *False*

-   a method called `first()` which reads the first element of the queue (without removing it)

Also modify the `dequeue()` method using the implemented `is_empty()` method in the conditional statement.


#### Example:


    [IN]: que = Queue()
    [IN]: que.enqueue('529')
    [IN]: que.enqueue('512')
    [IN]: len(que)
    [OUT]: 2
     
    [IN]: que.enqueue('844')
    [IN]: que.first()
    [OUT]: '529'
     
    [IN]: len(que)
    [OUT]: 3
     
    [IN]: que.is_empty()
    [OUT]: False


The tests run several test cases to validate the solution.