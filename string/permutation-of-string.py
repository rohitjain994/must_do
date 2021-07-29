class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(l,r):
            if l == r:
                res.append(nums[:])
            for i in range(l,r):
                nums[i],nums[l] = nums[l],nums[i]
                bt(l+1,r)
                nums[i],nums[l] = nums[l],nums[i]
            return
        res = []
        bt(0,len(nums))
        return res