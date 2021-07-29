def knapsack(v, w, n, W, lookup):
     
    # base case: Negative capacity
    if W < 0:
        return -sys.maxsize
 
    # base case: no items left or capacity becomes 0
    if n < 0 or W == 0:
        return 0
 
    # construct a unique key from dynamic elements of the input
    key = (n, W)
 
    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
        # Case 1. Include current item `v[n]` in the knapsack and recur for
        # remaining items `n-1` with decreased capacity `W-w[n]`
        include = v[n] + knapsack(v, w, n - 1, W - w[n], lookup)
 
        # Case 2. Exclude current item `v[n]` from the knapsack and recur for
        # remaining items `n-1`
        exclude = knapsack(v, w, n - 1, W, lookup)
 
        # assign the max value we get by including or excluding the current item
        lookup[key] = max(include, exclude)
 
    # return solution to the current subproblem
    return lookup[key]

def knapsack(v, w, W):
     
    # `T[i][j]` stores the maximum value of knapsack having weight less
    # than equal to `j` with only first `i` items considered.
    T = [[0 for x in range(W + 1)] for y in range(len(v) + 1)]
 
    # do for i'th item
    for i in range(1, len(v) + 1):
 
        # consider all weights from 0 to maximum capacity `W`
        for j in range(W + 1):
 
            # don't include the i'th element if `j-w[i-1]` is negative
            if w[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                # find the maximum value we get by excluding or including the i'th item
                T[i][j] = max(T[i - 1][j], T[i - 1][j - w[i - 1]] + v[i - 1])
 
    # return maximum value
    return T[len(v)][W]