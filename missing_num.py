# getMissingNo takes list as argument
def getMissingNo(A):
    n = len(A)
    x1 = A[0] # For xor of all the elements in array
    x2 = 1 # For xor of all the elements from 1 to n+1
    for i in range(n):
        x1 ^= A[i]
    for i in range(n+2):
        x2 ^= i
    return x1^x2
 
# Driver program to test above function
A = [1, 2, 3, 5, 6]
miss = getMissingNo(A)
print(miss)