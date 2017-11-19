"""
Microsoft

Rotate Linear Array
Time Complexity - O(n)
Space Complexity - O(n)

Rotate an array to the left by k positions without using extra space.k can be greater than the size of the array.

Example:
rotate_left([1,2,3,4,5],2) --> [3,4,5,1,2]
"""

# Space Complexity - O(n)
def rotate_left(list_numbers,k):
    lenList = len(list_numbers)
    start = k % lenList
    i = 0
    temp = []

    while(i != lenList):
        temp.append(list_numbers[start % lenList])
        start += 1
        i += 1

    list_numbers = temp
    return list_numbers


# Space Complexity - O(1)
def rotate_left(list_numbers, k):
    # yet to implement
    pass  
