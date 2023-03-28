

class IntDict(dict):
    
    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer.')
        return dict.__setitem__(self, key, value)