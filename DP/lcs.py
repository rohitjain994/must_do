def LCSLength(X, Y, m, n, lookup):
     
    # return if the end of either string is reached
    if m == 0 or n == 0:
        return 0
 
    # construct a unique key from dynamic elements of the input
    key = (m, n)
 
    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
 
        # if the last character of `X` and `Y` matches
        if X[m - 1] == Y[n - 1]:
            lookup[key] = LCSLength(X, Y, m - 1, n - 1, lookup) + 1
 
        else:
            # otherwise, if the last character of `X` and `Y` don't match
            lookup[key] = max(LCSLength(X, Y, m, n - 1, lookup),
                            LCSLength(X, Y, m - 1, n, lookup))
 
    # return the subproblem solution from the dictionary
    return lookup[key]

def LCSLength(X, Y):
     
    m = len(X)
    n = len(Y)
 
    # lookup table stores solution to already computed subproblems;
    # i.e., `T[i][j]` stores the length of LCS of substring
    # `X[0…i-1]` and `Y[0…j-1]`
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
    # LCS will be the last entry in the lookup table
    return T[m][n]