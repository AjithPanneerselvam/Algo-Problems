

def searchRotatedArray(A, element):
    start = 0
    end = len(A) - 1

    while (start < end):
        mid = (start + end) // 2
        
        if(A[mid] == element):
            return mid 
        
        if(element < A[mid] and element >= A[start]):
            end = mid - 1
        
        if(element > A[mid] and element <= A[end]):   
            start = mid + 1
        
        if(element < A[start] and element > A[mid]):
            start = mid + 1
        
        if(element < A[mid] and element < A[start]):
            end = mid - 1


A = [4, 5, 6, 7, 0, 1, 2]
print(searchRotatedArray(A, 1))
        


