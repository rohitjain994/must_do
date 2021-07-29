def LIS(A):
     
    # list to store subproblem solutions. `L[i]` stores the length
    # of the longest increasing subsequence that ends with `A[i]`
    L = [0] * len(A)
 
    # the longest increasing subsequence ending at `A[0]` has length 1
    L[0] = 1
 
    # start from the second element in the list
    for i in range(1, len(A)):
        # do for each element in sublist `A[0…i-1]`
        for j in range(i):
            # find the longest increasing subsequence that ends with `A[j]`
            # where `A[j]` is less than the current element `A[i]`
            if A[j] < A[i] and L[j] > L[i]:
                L[i] = L[j]
 
        # include `A[i]` in LIS
        L[i] = L[i] + 1
 
    # return longest increasing subsequence (having maximum length)
    return max(L)