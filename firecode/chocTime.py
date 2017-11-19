"""
#Google

Chocolate time!
Time Complexity - O(n)
Space Complexity - O(n)

There are N students standing in a line where each student has some points.
You distribute chocolates to these students under the following constraints:

   1. Each student must have at least one chocolate.
   2. Students with a higher point value get more chocolates than their neighbors.

Write a method distributeChocolate to compute the minimum number of chocolates distributed such that the above conditions are satisfied.

Example:

distributeChocolate("[1,5,7,1]") ==> 7

In this example, input is a list of points which 4 different students have been allotted. The minimum number of chocolates distributed i.e. the output is 7.
"""

# firecode solution
def distributeChocolate(points):
    if len(points) == 0:
        return 0
    numChocolates = [1]

    for i in range(1,len(points)):
        if points[i]>points[i-1]:
            numChocolates.append(numChocolates[i-1]+1)
        else:
            numChocolates.append(1)

    result = numChocolates[len(points)-1]
    for i in range(len(points)-2,-1,-1):
        if points[i]>points[i+1]:
            numChocolates[i] = max (numChocolates[i], numChocolates[i+1]+1)
        result += numChocolates[i]

    return result
