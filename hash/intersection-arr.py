class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))

# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((collections.Counter(nums1)&collections.Counter(nums2)).elements())
        
# https://leetcode.com/problems/intersection-of-two-arrays-ii/