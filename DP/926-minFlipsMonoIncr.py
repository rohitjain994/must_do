class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        p = [0]*(n+1)
        for i,c in enumerate(s):
            p[i+1]=p[i]+int(c)
        res = float('inf')
        for j in range(n+1):
            # 1 before j to be flipped + 0 after j to be flipped
            res = min(res,p[j]+n-j-(p[n]-p[j]))
        return res
        