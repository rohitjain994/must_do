class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def lsearch(x):
            l,r = 0,n-1
            res = -1
            while l<=r :
                m = (l+r)//2
                if x==nums[m]:
                    res = m
                    r = m-1
                elif x<nums[m]:
                    r = m-1
                else:
                    l = m+1
            return res
        def rsearch(x):
            l,r = 0,n-1
            res = -1
            while l<=r :
                m = (l+r)//2
                if x==nums[m]:
                    res = m
                    l = m+1
                elif x<nums[m]:
                    r = m-1
                else:
                    l = m+1
            return res
        lb = lsearch(target)
        if lb == -1:
            return [-1,-1]
        rb = rsearch(target)
        return [lb,rb]
                