class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0]*k
        for i in arr:
            cnt[i%k]+=1
        i,j=1,k-1
        res=0
        while i<j:
            if cnt[i]!=cnt[j]:
                return False
            res+=cnt[i]
            i+=1
            j-=1
        if res>0 and i==j:
            res+=cnt[i]//2
        res+=cnt[0]//2
        return res==len(arr)//2
    
            
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/