class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque([])
        ans = []
        for i in range(len(nums)):
            while dq and dq[-1]<nums[i]:
                dq.pop()
            dq.append(nums[i])
            if i>=k:
                if dq and dq[0] == nums[i-k]:
                    dq.popleft()
            if i>=k-1:
                ans.append(dq[0])
        return ans
        