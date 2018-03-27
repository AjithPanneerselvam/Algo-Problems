"""
Salesforce

The idea behind the classic Mergesort algorithm is to divide an array in half, sort each half, and merge the two halves into a single sorted list. 

Examples:
merge_sort([2,7,5,9,8,9]) -> [2,5,7,8,9,9]

merge_sort()([7,1,8,2]) -> [1,2,7,8]

merge_sort()([2]) -> [2]

[] -> [Empty] list 
"""

def merge_sort(a_list):
    if len(a_list)>1:
        mid = len(a_list)//2
        lefthalf = a_list[:mid]
        righthalf = a_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a_list[k]=lefthalf[i]
                i=i+1
            else:
                a_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            a_list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            a_list[k]=righthalf[j]
            j=j+1
            k=k+1
        
    return a_list
  