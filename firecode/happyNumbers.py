"""
Happy Numbers!

Write a method to determine whether a postive number is Happy.

A number is Happy (Yes, it is a thing!) if it follows a sequence that ends in 1 after following the steps given below :

Beginning with the number itself, replace it by the sum of the squares of its digits until either the number becomes 1 or loops endlessly in a cycle that does not include 1.
For instance, 19 is a happy number.
   Sequence:

      1^2 + 9^2 = 82

      8^2 + 2^2 = 68

      6^2 + 8^2 = 100

      1^2 + 0^2 + 0^2 = 1


Example:
Input : 19
Output: true
"""

def is_happy_number(number):

    if(len(str(number)) == 1):
        return False

    temp = number
    sqSum =  0
    while(temp):
        sqSum += (temp % 10)**2
        temp /= 10

    if sqSum == 1:
        return True

    return is_happy_number(sqSum)
