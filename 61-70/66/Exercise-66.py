
class NaturalList(list):
    
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer.')
        if not value > 0:
            raise ValueError('The value must be a natural number.')
        return list.append(self, value)