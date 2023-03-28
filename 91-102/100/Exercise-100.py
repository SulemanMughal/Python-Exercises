
class Queue:
    """The simplest queue."""
    
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def enqueue(self, item):
        self._data.append(item)
    
    def dequeue(self):
        if len(self._data) == 0:
            raise IndexError('The queue is empty.')
        return self._data.pop(0)