class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = None
        cnt =0
        for i in nums:
            if cnt ==0:
                num = i
            cnt += 1 if i == num else -1
        return num if nums.count(num)>len(nums)//2 else None