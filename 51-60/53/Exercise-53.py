
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
    
    
def encrypt(message):
    return ' '.join(
        [
            MORSE_CODE[char.upper()] if char != ' ' else '/'
            for char in message
        ]
    )
    
    
def decrypt(message):
    decipher = ''
    for char in message.split():
        if char != '/':
            decipher += MORSE_CODE_REVERSED[char]
        else:
            decipher += ' '
    return decipher


# Solution 2
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
    
    
def encrypt(message):
    return ' '.join(
        [
            MORSE_CODE[char.upper()] if char != ' ' else '/'
            for char in message
        ]
    )
    
    
def decrypt(message):
    return ''.join(
        [
            MORSE_CODE_REVERSED[char] if char != '/' else ' '
            for char in message.split()
        ]
    )