
from itertools import groupby
    
    
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, len(list(group))))
    return result
    
def compress(number):
    return [(key, len(list(group))) for key, group in groupby(str(number))]