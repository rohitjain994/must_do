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

class Solution:
    def minInsertions(self, S: str) -> int:
        n = len(S)
        dp = [[-1]*n for _ in range(n)]
        def ok(s,e):
            if s>=e:
                return 0
            if dp[s][e]!=-1:
                return dp[s][e]
            if S[s]==S[e]:
                dp[s][e]= ok(s+1,e-1)
            else:
                dp[s][e] = 1+ min(ok(s,e-1),ok(s+1,e))
            return dp[s][e]
        
        return ok(0,n-1)
            
            