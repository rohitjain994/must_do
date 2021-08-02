class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        fmap = collections.Counter(nums)
        return sorted(nums,key=lambda x:(fmap[x],-x))

# https://leetcode.com/problems/sort-array-by-increasing-frequency/
# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.