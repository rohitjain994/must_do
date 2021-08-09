class Solution:
    def findIntegers(self, n: int) -> int:
        f = [0]*32
        f[0] = 1
        f[1] = 2
        for i in range(2,32):
            f[i] = f[i-1]+f[i-2]
        res = 0
        prv = 0
        i = 30
        while i>=0 :
            if (n & (1<<i))!=0:
                res += f[i]
                if prv == 1:
                    res -=1
                    break
                prv = 1
            else:
                prv = 0
            i-=1
        return res+1