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
                