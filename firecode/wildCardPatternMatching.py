"""
Google

Wildcard Pattern Matching
Time Complexity - O(m * n)
Space Complexity - O(m * n)

You are given two strings - where the first string can include regex wildcard characters (* and ?)
and other is a regular string.
Write a method to check if the two strings match.

* --> Matches with zero or more characters.

? --> Matches exactly a single character.

Examples:

match("fi*de", "firecode") ==> "True"
match("fi?de", "firecode") ==> "False"
"""

def match(first, second = ""):
    pattern = first
    stringVal = second

    # Remove the consequent redundant '*' to simplify the problem
    i = 0
    patternLength = len(pattern)
    resultPattern = ""

    while i < patternLength:
        if pattern[i] == '*':
            resultPattern += pattern[i]
            while(i < patternLength and pattern[i] == '*'):
                i += 1
        else:
            resultPattern += pattern[i]
            i += 1
    pattern = resultPattern

    # Initial setup
    dynTable =[ [False for j in range(len(pattern) + 1)] for i in range(len(stringVal) + 1)]
    dynTable[0][0] = True
    for j in range(1, len(pattern)+ 1):
        # if pattern[j-1] == '*':
        #     dynTable[0][j] = True
        # else:
        dynTable[0][j] = False
    for i in range(1, len(stringVal) + 1):
        dynTable[i][0] = False

    # print(dynTable)

    for i in range(1, len(stringVal) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j -1] == '?' or stringVal[i - 1] == pattern[j - 1]:
                dynTable[i][j] = dynTable[i - 1][j - 1]
            elif pattern[j -1] == '*':
                dynTable[i][j] = dynTable[i][j-1] or dynTable[i-1][j]

    print(dynTable[len(stringVal)][len(pattern)])
    print(dynTable)

# pattern = input()
# match("a**b","ab")
# match("a*?b", "abbbcb")
# match("a*?b", "ab")
# match("*i?e*d?", "firecode")
match("?i?e*d?", "fairecode")


#firecode solution
def match(first, second):
    l = 0; m = 0; starIdx = -1;i = -1;
    while l < len(second):
        if m < len(first) and (first[m] == '?' or first[m] == second[l]) :
            m += 1
            l += 1
        elif m < len(first) and first[m] == '*' :
            i = l
            starIdx = m
            m += 1
        elif starIdx != -1 :
            l = i+1
            m = starIdx + 1
            i += 1
        else :
            return False
    while m < len(first) and first[m] == '*':
        m += 1
    return m == len(first)
