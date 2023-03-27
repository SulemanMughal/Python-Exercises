# Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes.

# All characters are represented by a series of signals of several elements - short (dots) and long (dashes). The duration of the dash is at least three times the duration of the dot.

# We also need to add spaces in encrypted messages. The space between the elements of the sign should be one dot. Space between individual characters - three dots and space between groups of characters (words) - seven dots.

# We only use capital letters of the alphabet.

# Dictionary mapping characters to Morse code:


#     MORSE_CODE = {
#         'A': '.-',
#         'B': '-...',
#         'C': '-.-.',
#         'D': '-..',
#         'E': '.',
#         'F': '..-.',
#         'G': '--.',
#         'H': '....',
#         'I': '..',
#         'J': '.---',
#         'K': '-.-',
#         'L': '.-..',
#         'M': '--',
#         'N': '-.',
#         'O': '---',
#         'P': '.--.',
#         'Q': '--.-',
#         'R': '.-.',
#         'S': '...',
#         'T': '-',
#         'U': '..-',
#         'V': '...-',
#         'W': '.--',
#         'X': '-..-',
#         'Y': '-.--',
#         'Z': '--..',
#         '1': '.----',
#         '2': '..---',
#         '3': '...--',
#         '4': '....-',
#         '5': '.....',
#         '6': '-....',
#         '7': '--...',
#         '8': '---..',
#         '9': '----.',
#         '0': '-----',
#         '&': '.-...',
#         '@': '.--.-.',
#         ':': '---...',
#         ',': '--..--',
#         '.': '.-.-.-',
#         ''': '.----.',
#         ''': '.-..-.',
#         '?': '..--..',
#         '/': '-..-.',
#         '=': '-...-',
#         '+': '.-.-.',
#         '-': '-....-',
#         '(': '-.--.',
#         ')': '-.--.-',
#         '!': '-.-.--',
#     }


# The letters 'a' and 'A' have the same code '.-'.


# Example:


#     [message]: 'PYTHON 3.9'
#     [morse code]: '.--. -.-- - .... --- -. / ...-- .-.-.- ----.'


# Example:


#     [message]: 'HOLD YOUR POSITIONS!'
#     [morse code]: '.... --- .-.. -.. / -.-- --- ..- .-. / .--. --- ... .. - .. --- -. ... -.-.--'


# Implement a solution to this problem using the object-oriented programming (OOP) paradigm. Create a class named MorseCode that contains two static methods (use the @staticmethod decorator):

#     encrypt() - a method that encrypts message into Morse code

#     decrypt() - a method that decrypts the message


# Example:


#     [IN]: MorseCode.encrypt('HOLD!')
#     [OUT]: '.... --- .-.. -.. -.-.--'
     
#     [IN]: MorseCode.decrypt('.... --- .-.. -.. -.-.--')
#     [OUT]: 'HOLD!'


# You only need to implement the MorseCode class. 


MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '&': '.-...',
    '@': '.--.-.',
    ':': '---...',
    ',': '--..--',
    '.': '.-.-.-',
    ''': '.----.',
    ''': '.-..-.',
    '?': '..--..',
    '/': '-..-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    '!': '-.-.--',
}
    
MORSE_CODE_REVERSED = {val: key for key, val in MORSE_CODE.items()}
    
    
class MorseCode:
    
    @staticmethod
    def encrypt(message):
        return ' '.join(
            [
                MORSE_CODE[char.upper()] if char != ' ' else '/'
                for char in message
            ]
        )
    
    @staticmethod
    def decrypt(message):
        return ''.join(
            [
                MORSE_CODE_REVERSED[char] if char != '/' else ' '
                for char in message.split()
            ]
        )