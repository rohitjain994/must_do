from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums,path,tar):
            if tar<0:
                return
            if tar==0:
                res.append(path[:])
                return
            for i in range(len(nums)):
                dfs(nums[i:],path+[nums[i]],tar-nums[i])
        dfs(candidates,[],target)
        return res
# complexity = O(2^n)
class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums,path,tar):
            if tar<0:
                return
            if tar==0:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                dfs(nums[i+1:],path+[nums[i]],tar-nums[i])
        dfs(sorted(candidates),[],target)
        return res
# complexity = O(2^n)