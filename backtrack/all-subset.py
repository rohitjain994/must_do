from typing import List
import math

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        N = int(math.pow(2,n))
        _set = set()
        nums.sort()
        for i in range(N):
            sub = []
            for j in range(n):
                if i&(1<<j):
                    sub.append(nums[j])
            # print(tuple(sub))
            _set.add(tuple(sub))
        return _set
                    