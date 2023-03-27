# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
# Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, ...
# Implement a function called is_prime() that takes a natural number as an argument and checks if it is a prime number. In the case of a prime number, the function returns True, otherwise False.

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True