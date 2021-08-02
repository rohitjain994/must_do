class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hasmap = {e:i for i,e in enumerate(arr2)}
        return sorted(arr1,key=lambda x:hasmap.get(x,1000+x))


# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]