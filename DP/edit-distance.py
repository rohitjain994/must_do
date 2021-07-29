# Function to find Levenshtein distance between string `X` and `Y`.
def dist(X, Y):
    # `m` and `n` is the total number of characters in `X` and `Y`, respectively
    (m, n) = (len(X), len(Y))
 
    # For all pairs of `i` and `j`, `T[i, j]` will hold the Levenshtein distance
    # between the first `i` characters of `X` and the first `j` characters of `Y`.
    # Note that `T` holds `(m+1)×(n+1)` values.
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
    # we can transform source prefixes into an empty string by
    # dropping all characters
    for i in range(1, m + 1):
        T[i][0] = i                    # (case 1)
 
    # we can reach target prefixes from empty source prefix
    # by inserting every character
    for j in range(1, n + 1):
        T[0][j] = j                    # (case 1)
 
    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
 
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:            # (case 2)
                cost = 0                        # (case 2)
            else:
                cost = 1                        # (case 3c)
 
            T[i][j] = min(T[i - 1][j] + 1,      # deletion (case 3b)
                        T[i][j - 1] + 1,        # insertion (case 3a)
                        T[i - 1][j - 1] + cost) # replace (case 2 + 3c)
 
    return T[m][n]
 
 
if __name__ == '__main__':
 
    X = "kitten"
    Y = "sitting"
 
    print("The Levenshtein distance is", dist(X, Y))

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                elif word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]