class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        maxl = 1
        for i in range(n):
            dp[i][i]=1 # True 
        start = 0
        for i in range(0,n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
                start = i
                maxl = 2
        for k in range(3,n+1):
            for i in range(0,n-k+1):
                j = i+k-1
                if dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j]=1
                    if k>maxl:
                        maxl=k
                        start=i
        return s[start:start+maxl]