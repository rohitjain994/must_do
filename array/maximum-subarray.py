class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #2pointer
        n = len(nums)
        if n <=0:
            return 0
        msum = esum = nums[0]
        
        for i in range(1,n):
            esum = max(nums[i],esum+nums[i])
            msum = max(msum,esum)
        return msum
                
        

# Kaddanes algorithm