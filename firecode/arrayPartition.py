"""
Array Partition
Time-Complexity - O(n)
Space-Complexity - O(n)

Given a sorted list of integers, find partitions such that each partition denotes a range of consecutive integers.
Note: The input list consists of sorted integers, without duplicates. Range(a,b) should be denoted as a-b where a and b are included in the range.

Example:
Input : [1,2,3,6,7,8,10,11]
Output : [1-3, 6-8, 10-11]
"""

def find_partitions(input_list):
    outputList = [input_list[0]]
    startRange = 0

    for i in range(1, len(input_list)):
        if input_list[i] - input_list[i-1] != 1 and startRange != i-1:
            outputList[-1] = str(outputList[-1]) +  '-' + str(input_list[i-1])
            startRange = i
            outputList.append(input_list[i])
        elif input_list[i] - input_list[i-1] != 1:
            startRange = i
            outputList.append(input_list[i])

    if input_list[-1] - input_list[-2] == 1:
        outputList[-1] = str(outputList[-1]) + '-' + str(input_list[-1])


    return outputList
