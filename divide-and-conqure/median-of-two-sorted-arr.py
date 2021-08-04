class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        l = len(a)+len(b)
        if l&1:
            return self.kth(a,b,l//2)
        return (self.kth(a,b,l//2)+self.kth(a,b,l//2-1))/2
    def kth(self,a,b,k):
        if not a: return b[k]
        if not b: return a[k]
        ia,ib = len(a)//2,len(b)//2
        if ia+ib<k:
            if a[ia]>b[ib]:
                return self.kth(a,b[ib+1:],k-ib-1)
            else:
                return self.kth(a[ia+1:],b,k-ia-1)
        else:
            if a[ia]>b[ib]:
                return self.kth(a[:ia],b,k)
            else:
                return self.kth(a,b[:ib],k)
            

# https://leetcode.com/problems/median-of-two-sorted-arrays/