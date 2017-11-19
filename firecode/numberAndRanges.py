"""
Given a sorted list and an input number as inputs, write a function to return a Range object, consisting of the indices of the first and last occurrences of the input number in the list. Check out the Use Me section to examine the structure of the Range class.

Note: The List can have duplicate numbers. The indices within the Range object should be zero based.

Examples:
Input List  : [1,2,5,5,8,8,10]
Input Number : 8
Output : [4,5]
"""

def find_range(input_list,input_number):
    i = 0
    flag = False

    while i < len(input_list):
        if flag == False and input_list[i] == input_number:
            result = Range(i,i)
            lastOccurrence = i
            flag = True
        elif input_list[i] == input_number:
            lastOccurrence = i

        i += 1

    result.upper_bound = lastOccurrence
    return result
