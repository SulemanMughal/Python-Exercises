# Consider the palindromic numbers. A palindromic or symmetric number is a number that does not change when you write its digits in reverse order.
# Some examples of palindromic numbers:
#     363
#     2882
#     29492
# A function called is_palindrome() is implemented that checks if the number is palindromic in decimal and binary notation.
# Implement a function called calculate() that returns all three-digit palindromic numbers in both decimal and binary notation. In response, call calculate() function and print the result to the console.



def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]
    
    
def calculate():
    return [i for i in range(100, 1000) if is_palindrome(i)]
    
    
print(calculate())

def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]
    
    
def calculate():
    return list(filter(is_palindrome, [i for i in range(100, 1000)]))
    
    
print(calculate())