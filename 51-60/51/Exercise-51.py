
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