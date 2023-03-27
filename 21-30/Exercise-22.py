# Consider the popular Scrabble game. Scrabble is a word game in which players score points by placing tiles, each bearing a single letter, onto a game board divided into a 15×15 grid of squares. The tiles must form words that, in crossword fashion, read left to right in rows or downward in columns, and be included in a standard dictionary or lexicon.

# The combined words are scored, and the game is won by the player who in total (in all moves) scores more points than each of the opponents. The number of points is calculated based on the letters in each word. Each letter has a specific, fixed point value.

# Below are the scores for the English version:

#     blank tile - 0 pt (usually two in a set)

#     EAIONRTLSU - 1 pt

#     DG - 2 pt

#     BCMP - 3 pt

#     FHVWY - 4 pt

#     K - 5 pt

#     JX - 8 pt

#     QZ - 10 pt

# Implement a function called score() that returns a result for one word. We assume that the given word is grammatically correct. We can represent a blank tile for simplicity as a space character ' '.


# Tip: We can use the built-in collections module and the ChainMap class.


# Example:


#     [IN]: score('python')
#     [OUT]: 14


# Example:


#     [IN]: score('programming')
#     [OUT]: 19

from collections import ChainMap
    
    
english_scoreboard = {
    ' ': 0,
    'EAIONRTLSU': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10,
}
    
    
def score(word):
    scores = ChainMap(
        *[
            dict.fromkeys(letter, score)
            for letter, score in english_scoreboard.items()
        ]
    )
    return sum([scores[letter.upper()] for letter in word])


letters = {
    ' ': 0,
    'E': 1,
    'A': 1,
    'I': 1,
    'O': 1,
    'N': 1,
    'R': 1,
    'T': 1,
    'L': 1,
    'S': 1,
    'U': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10
}
    
    
def score(word):
    return sum([letters[letter.upper()] for letter in word])