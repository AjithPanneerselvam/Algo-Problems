def isPrime(A):
    if(A == 1 or A == 0):
        return 0
        
    if(A <= 3):
        return 1
    
    upperLimit = int(A**0.5)

	    
    for i in range(2, upperLimit + 1):
        if i < A and A % i == 0:
            return 0
    return 1


print(isPrime(2))