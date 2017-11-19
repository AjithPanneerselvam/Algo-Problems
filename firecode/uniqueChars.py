"""
Microsoft

Unique Chars in a String
Write a function that takes in an input string and returns True if all the characters in the string are unique, False if there is even a single repeated character.

Examples:

unique_chars_in_string("abcde") -> True

unique_chars_in_string("aa") -> False
"""

def unique_chars_in_string(input_string):
    charList = list(input_string)
    asciiSet = [0 for i in range(256)]

    for char in charList:
        if asciiSet[ord(char)] == 1:
            return False
        else:
            asciiSet[ord(char)] = 1

    return True
