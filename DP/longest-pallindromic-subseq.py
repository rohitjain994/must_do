def longestPalindrome(X, i, j, lookup):
     
    # Base condition
    if i > j:
        return 0
 
    # If the string `X` has only one character, it is a palindrome
    if i == j:
        return 1
 
    # construct a unique key from dynamic elements of the input
    key = (i, j)
 
    # If the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
 
        ''' If the last character of the string is the same as the first character,
            include the first and last characters in palindrome and recur
            for the remaining substring X[i+1, j-1] '''
 
        if X[i] == X[j]:
            lookup[key] = longestPalindrome(X, i + 1, j - 1, lookup) + 2
        else:
            ''' If the last character of the string is different from the
                first character
 
                1. Remove the last character recur for the remaining substring
                   `X[i, j-1]`
                2. Remove the first character recur for the remaining substring
                   `X[i+1, j]`
                3. Return the maximum of the two values '''
 
            lookup[key] = max(longestPalindrome(X, i, j - 1, lookup),
                            longestPalindrome(X, i + 1, j, lookup))
 
    # Return the subproblem solution from the dictionary
    return lookup[key]