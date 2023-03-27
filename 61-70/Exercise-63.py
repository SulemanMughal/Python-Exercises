#     lambda x, y: x + y, ['p', 'y', 't', 'h', 'o', 'n'])
#     [OUT]: 'python'


# Example:


#     [IN]: reduce(lambda x, y: x + y, [[3, 4], [8, 4], [9, 1]])
#     [OUT]: [3, 4, 8, 4, 9, 1]


# You just need to implement the reduce() function. 



def reduce(function, iterable):
    if len(iterable) == 0:
        return None
    result = iterable[0]
    for item in iterable[1:]:
        result = function(result, item)
    return result