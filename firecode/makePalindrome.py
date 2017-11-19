"""
Microsoft
Time-Complexity - O(n^2)
Space-Complexity - O(n)

Make Palindrome
Given a string as the input, append characters to it to make it into a palindrome. Return this new palindrome.
Note: If the input is a palindrome then it should be returned as is.

Example:
Input  : race
Output : racecar
"""

def make_palindrome(input):
    if input == input[::-1]:
        return input

    for i in range(len(input) - 2, -1, -1):
        input = input + input[i]
        if input == input[::-1]:
            return input
