class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # a = set(arr)
        # i =1
        # while k > 0:
        #     if i not in a:
        #         k -= 1
        #     if k == 0:
        #         return i
        #     i += 1
        # return -1
        n = len(arr)
        l,r=0,n
        while l<r:
            m = (l+r)//2
            if arr[m]-(m+1)<k:
                l = m+1
            else:
                r = m
        return r+k
            
                
            
        