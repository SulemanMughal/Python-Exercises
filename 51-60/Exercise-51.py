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

# The CaesarCipher class is given:


#     class CaesarCipher:
     
#         def __init__(self, alphabet, key):
#             self.alphabet = alphabet
#             self.key = key
     
#         @property
#         def cipher(self):
#             result = ''
#             for letter in self.alphabet:
#                 new_idx = (self.alphabet.index(letter) + self.key) % len(self.alphabet)
#                 result += self.alphabet[new_idx]
#             return result


# Follow the next steps in this exercise:

#     Implement an encrypt() method that encrypts the message (message argument)

#     Implement a decrypt() method that decrypts the message (message argument)


# You just need to implement these methods. 


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
    
    def encrypt(self, message):
        result = ''
        for letter in message:
            if letter not in self.alphabet:
                result += letter
            else:
                result += self.cipher[
                    self.alphabet.index(letter)
                ]
        return result
    
    def decrypt(self, message):
        result = ''
        for letter in message:
            if letter not in self.alphabet:
                result += letter
            else:
                result += self.alphabet[
                    self.cipher.index(letter)
                ]
        return result