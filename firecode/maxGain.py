"""
Bloomberg

Max Gain
Given an list of integers, write a method - max_gain - that returns the maximum gain. Maximum Gain is defined as the maximum difference between 2 elements in a list such that the larger element appears after the smaller element. If no gain is possible, return 0.

Example:
max_gain([100,40,20,10]) ==> 0
max_gain([0,50,10,100,30]) ==> 100
"""

def max_gain(input_list):
    max_gain = 0
    smallestElement = input_list[0]

    for i in range(1, len(input_list)):

        if input_list[i] - smallestElement > max_gain and input_list[i] - smallestElement > 0:
            max_gain = input_list[i] - smallestElement

        if smallestElement > input_list[i]:
            smallestElement = input_list[i]

    return max_gain
