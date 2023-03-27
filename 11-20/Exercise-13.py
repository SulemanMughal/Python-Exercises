# Consider a simple number compression algorithm that works as follows:
#     111155522500 -> '14_53_22_51_02'
# The algorithm goes from left to right through the number and returns an object of type str. Each encountered digit is stored along with the number of times that digit repeats until another digit is encountered in the number. Each such pair is separated by the '_' character.
# Implement a function called compress() that compresses number as described above.


from itertools import groupby
    
    
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)



def compress(number):
    result = [''.join((key, str(len(list(group))))) for key, group in groupby(str(number))]
    return '_'.join(result)