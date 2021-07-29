def minDeletions(X, i, j, lookup):
     
    # base condition
    if i >= j:
        return 0
 
    # construct a unique key from dynamic elements of the input
    key = (i, j)
 
    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
 
        # if the last character of the string is the same as the first character
        if X[i] == X[j]:
            lookup[key] = minDeletions(X, i + 1, j - 1, lookup)
        else:
            # if the last character of the string is different from the first character
 
            # 1. Remove the last character and recur for the remaining substring
            # 2. Remove the first character and recur for the remaining substring
 
            # return 1 (for remove operation) + minimum of the two values
 
            result = 1 + min(minDeletions(X, i, j - 1, lookup),
                                minDeletions(X, i + 1, j, lookup))
            lookup[key] = result
 
    # return the subproblem solution from the dictionary
    return lookup[key]