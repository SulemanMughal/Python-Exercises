
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