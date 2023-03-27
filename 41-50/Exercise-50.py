# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the string is replaced by a letter some fixed number of positions down the alphabet.

# An example of the encryption. Consider only capital letters in English (let's just call it alphabet):


#     ABCDEFGHIJKLMNOPQRSTUVWXYZ


# Shifting the above alphabet by a certain number (key = 2) gives us the cipher:


#     CDEFGHIJKLMNOPQRSTUVWXYZAB


# Let's put it together:


#     ABCDEFGHIJKLMNOPQRSTUVWXYZ
#     CDEFGHIJKLMNOPQRSTUVWXYZAB


# Note that for the last letters of the alphabet (Y, Z) the initial letters are matched.

# Having an alphabet and a cipher, we can start encrypting. Consider the message below:


#     'ATTACK AT DAWN!'


# Using the Caesar cipher with an offset of 2 (key = 2) we get:


#     'CVVCEM CV FCYP!'


# Implement a solution to this problem using the object-oriented programming (OOP) paradigm.

# Steps to do in this exercise:

#     Create a class named CaesarCipher

#     In the __init__() method set two instance attributes: alphabet and key.

#     Implement a read-only property called cipher that stores the cipher

# You only need to implement CaesarCipher class. 


class CaesarCipher:
    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key
    
    @property
    def cipher(self):
        result = ''
        for letter in self.alphabet:
            new_idx = (
                self.alphabet.index(letter) + self.key
            ) % len(self.alphabet)
            result += self.alphabet[new_idx]
        return result