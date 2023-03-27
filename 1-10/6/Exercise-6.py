def calculate():
    numbers = []
    for i in range(10, 100):
        for j in range(10, 100):
            if str(i * j) == str(i * j)[::-1]:
                numbers.append(i * j)
    return max(numbers)
    
    
print(calculate())


def calculate():
    result = max([i * j
                    for i in range(10, 100)
                    for j in range(10, 100)
                    if str(i * j) == str(i * j)[::-1]])
    return result
    
    
print(calculate())