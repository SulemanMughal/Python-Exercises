
class IntList(list):
    
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer.')
        return list.append(self, value)