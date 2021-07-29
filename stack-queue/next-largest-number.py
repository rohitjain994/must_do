class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nummap = {e:i for i,e in enumerate(nums2)}
        nxtgr = [-1]*len(nums2)
        stack=[]
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                nxtgr[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i)
        # print(nxtgr,nummap)
        return [nxtgr[nummap[i]] for i in nums1]