"""
Google
Power of 4

Write a method to determine whether a given integer (zero or positive number) is a power of 4 without using the multiply or divide operator. If it is, return True, else return False.

Examples:
is_power_of_four(5) ==> False

is_power_of_four(16) ==> True

Hint: An integer is considered to be a power of 4 if
    1) it is one or 
    2) there is only one bit set in its binary representation and the number of bits to the right of the set bit is even.
"""

def is_power_of_four(number):
    if (number & (number - 1) == 0):
        temp = 1
        count = 0
        while ((number | temp) != number):
            count += 1
            temp <<= 1
        if (not(count % 2)):
            return True
        return False
    else:
        return False
