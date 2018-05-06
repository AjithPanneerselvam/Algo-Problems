"""
Given a string, return whether string is valid or invalid. A valid string is one which has each 
character repeating the same no of times as any other character. Also, if, at most one character 
appears unmatched no of times than rest of the characters, its also a valid string. All other strings are invalid.
"""

def isValidString(string):
    if(len(string) == 0 or len(string) == 1):
        return 1 
    
    x = y = -1
    misMatch = False 
    dictionary = {}

    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    
    x = dictionary[string[0]]

    for key in dictionary:
        if(x == dictionary[key] or y == dictionary[key]):
            continue
        elif (x != dictionary[key] and misMatch == False):
            misMatch = True 
            y = dictionary[key]
        else:
            return 0 
    
    return 1 


string = input()
print(isValidString(string))