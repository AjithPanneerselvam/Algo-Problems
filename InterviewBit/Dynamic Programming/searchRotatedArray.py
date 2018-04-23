def findPivot(A):
    start = 0
    end = len(A) -1

    if(A[start] < A[end]):
        return start

    while(start < end):
        mid = (start + end) // 2
        
        if(A[start] <= A[mid]):
            if(A[mid + 1] < A[mid]):
                return mid + 1
            start = mid 
        
        if(A[start] > A[mid]):
            if(mid - 1 >= 0 and A[mid-1] > A[mid]):
                return mid 
            end = mid 


# print(findPivot([5,6,7,8,0,1,4]))
# print(findPivot([6,7,8,0,1,4,5]))
# print(findPivot([8,0,1,4,5,6,7]))
# print(findPivot([2,4,5,6,7,0,1]))
# print(findPivot([6,7,0,1,2,4,5]))
# print(findPivot([4,5,6,7,0,1,2]))


def binarySearch(A, element, start, end):

    while(start <= end): 
        mid = (start + end) // 2
        
        if(A[mid] == element):
            return mid 
        if(element < A[mid]):
            end = mid - 1
        else:
            start = mid + 1
    
    return -1



def searchRotatedArray(A, element):
    # O(log n)
    pivot = findPivot(A)
    print("Pivot ", pivot)
    if(A[pivot] == element):
        return pivot
    
    if(A[pivot] < element and element <= A[len(A)-1]):
        # O(log n)
        return binarySearch(A, element, pivot + 1, len(A) - 1)
    else:
        # O(log n)
        return binarySearch(A, element, 0, pivot -1)



# A = [4, 5, 6, 7, 0, 1, 2]
# print(searchRotatedArray(A, 1))
# A = [6, 7, 0, 1, 2, 4, 5]
# print(searchRotatedArray(A,4))
# A = [6, 7, 0, 1, 2, 4, 5]
# print(searchRotatedArray(A,0))
# A = [6, 7, 0, 1, 2, 4, 5]
# print(searchRotatedArray(A,7))
# A = [1, 7, 67, 133, 178 ]
# print(searchRotatedArray(A,1))


        


