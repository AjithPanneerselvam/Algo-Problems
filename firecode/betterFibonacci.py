"""
Twitter

Better Fibonacci New
The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... The next number is found by adding up the two numbers before it.

Your goal is to write an optimal method - better_fibonacci that returns the nth Fibonacci number in the sequence. n is 0 indexed, which means that in the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., n == 0 should return 0 and n == 3 should return 2. Your method should exhibit a runtime complexity of O(n) and use constant O(1) space. With this implementation, your method should be able to compute larger sequences where n > 40.


Examples:

better_fibonacci(0) ==> 0
better_fibonacci(2) ==> 1
"""

def better_fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        x,y = y,y+x
    return x
