# Find minimum jumps required to reach the destination
def findMinJumps(A):
 
    # base case: the destination is unreachable from the source
    if A[0] == 0:
        return sys.maxsize
 
    # get length of the list
    n = len(A)
 
    # `lookup[i]` stores the minimum jumps required to reach `A[i]` from source `A[0]`
    lookup = [sys.maxsize] * n
 
    # destination is the same as the source
    lookup[0] = 0
 
    # do for every position
    for i in range(n):
 
        # find the minimum jumps required to reach the destination by
        # considering the minimum from each position reachable from `A[i]`
        j = 1
        while (i + j < n) and j <= min(n - 1, A[i]):
            lookup[i + j] = min(lookup[i + j], lookup[i] + 1) \
                if (lookup[i + j] != sys.maxsize) else (lookup[i] + 1)
            j = j + 1
 
    # `lookup[n-1]` would have the result since `A[n-1]` is the destination
    return lookup[n - 1]