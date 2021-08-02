class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hasmap = collections.defaultdict(int)
        psum = 0
        mmax = 0
        for i in range(len(nums)):
            psum +=nums[i] if nums[i] else -1
            if psum ==0:
                mmax = max(mmax,i+1) 
            if psum in hasmap:
                mmax = max(mmax,i-hasmap[psum])
            else:
                hasmap[psum] = i
        return mmax
            
# https://leetcode.com/problems/contiguous-array/          
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.