# Binary number system is a positional numeral system employing 2 as the base and so requiring only two different symbols for its digits, 0 and 1, instead of the usual 10 different symbols needed in the decimal system. The numbers from 0 to 10 are thus in binary 0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, and 1010.

# For example, the number 10 in binary can be represented as 1010 because:

# 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 8 + 0 + 2 + 0 = 10


# A function called decimal_to_binary() that converts a number from decimal to binary has been implemented:


#     def decimal_to_binary(number):
#         if number == 0:
#             return '0'
#         result = ''
#         while number > 0:
#             result += str(number % 2)
#             number = number // 2
#         return result[::-1]


# Now consider a bitwise OR operation on binary numbers. The operation is applied to pairs of natural numbers by performing operations on the digits of the binary notation of these numbers. A bitwise OR takes two bit patterns of equal length and performs the logical OR operation on each pair of corresponding bits. The result in each position is 0 if both bits are 0, while otherwise the result is 1. For example:


#     00001010
#     10001100
#     --------
#     10001110


# The above decimal numbers are 10 and 140. Where the binary number is shorter, we put extra zeros on the left side to perform the operation. The result of this operation is the number 10001110, which is the number 142 in decimal notation. We can write the whole operation as follows:


#     10 | 140 = 142


# Implement a function called bitwise_or() that takes two decimal numbers as arguments and returns the result of the bitwise OR operation in decimal. You can use int() to convert a number from binary to decimal. In case any of the arguments are less than zero raise the ValueError with the message:


#     'Both numbers must be positive.'


# Example:


#     [IN]: bitwise_or(10, 140)
#     [OUT]: 142


# Example:


#     [IN]: bitwise_or(10, 3)
#     [OUT]: 11


# Example:


#     [IN]: bitwise_or(-10, 3)
#     [OUT]: ValueError: Both numbers must be positive.


# You just need to implement the bitwise_or() function. 



def decimal_to_binary(number):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        result += str(number % 2)
        number = number // 2
    return result[::-1]
    
    
def bitwise_or(a, b):
    if a < 0 or b < 0:
        raise ValueError('Both numbers must be positive.')
    
    a_bin = decimal_to_binary(a)
    b_bin = decimal_to_binary(b)
    
    max_length = max(len(a_bin), len(b_bin))
    
    a_zfill = a_bin.zfill(max_length)
    b_zfill = b_bin.zfill(max_length)
    
    binary_or = [
        str(int(char_a == '1' or char_b == '1'))
        for char_a, char_b in zip(a_zfill, b_zfill)
    ]
    
    binary_result = ''.join(binary_or)
    decimal_result = int(binary_result, base=2)
    
    return decimal_result