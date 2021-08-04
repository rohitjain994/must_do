class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        # print(nset)
        res = 0
        for num in nset:
            if num-1 not in nset:
                cs = 1
                curr = num
                while curr + 1 in nset:
                    curr+=1
                    cs+=1
                res = max(res,cs)
        return res
                
# https://leetcode.com/problems/longest-consecutive-sequence/submissions/
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.