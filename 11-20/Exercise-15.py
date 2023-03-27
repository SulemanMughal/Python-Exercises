# Consider a simple number compression algorithm that works as follows:
#     111155522500 -> '14_53_22_51_02'
# The algorithm goes from left to right through the number and returns an object of str type. Each encountered digit is stored along with the number of times that digit repeats until another digit is encountered in the number. Each such pair is separated by the '_' character.
# A function called compress() is implemented that compresses a number as described above:
#     from itertools import groupby
#     def compress(number):
#         result = []
#         for key, group in groupby(str(number)):
#             result.append((key, str(len(list(group)))))
#         result = [''.join(item) for item in result]
#         return '_'.join(result)
# Implement a function called decompress() that decompresses the expression to a number.
# Examples:
#     [IN]: decompress('14_53_22_51_02')
# Consider a simple number compression algorithm that works as follows:
# 111155522500 -> '14_53_22_51_02'
# The algorithm goes from left to right through the number and returns an object of str type. Each encountered digit is stored along with the number of times that digit repeats until another digit is encountered in the number. Each such pair is separated by the '_' character.
# A function called compress() is implemented that compresses a number as described above:
#     from itertools import groupby
     
     
#     def compress(number):
#         result = []
#         for key, group in groupby(str(number)):
#             result.append((key, str(len(list(group)))))
#         result = [''.join(item) for item in result]
#         return '_'.join(result)
# Implement a function called decompress() that decompresses the expression to a number.
# Examples:
#     [IN]: decompress('14_53_22_51_02')
#     [OUT]: 111155522500
#     [IN]: decompress('11_03_51_03')
#     [OUT]: 10005000
#     [OUT]: 111155522500
#     [IN]: decompress('11_03_51_03')
#     [OUT]: 10005000

from itertools import groupby
    
    
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)
    
    
def decompress(compressed):
    result = [(item[0], item[1:]) for item in compressed.split('_')]
    result = [i * int(j) for i, j in result]
    return int(''.join(result))