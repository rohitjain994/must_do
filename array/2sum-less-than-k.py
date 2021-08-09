class Solution(object):
    def twoSumLessThanK(self, nums, target):

        if not nums and not target:
            return [ ]
        
        stack = [0] * 2 
        nums.sort()
        total = 0
        left, right = 0, len(nums)-1
        
        while left < right:
            sum = nums[left] + nums[right]
            if sum >= target:
                right -= 1
                
            else:
                if sum > total:
                    stack[0] = nums[left]
                    stack[1] = nums[right]
                    total = sum
                 left += 1               
        return stack