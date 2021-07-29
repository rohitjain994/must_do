# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cnt = 0
        curr = head
        while cnt<k:
            if not curr: return head
            curr = curr.next
            cnt+=1
        prv = self.reverseKGroup(curr,k)
        while cnt>0:
            succ = head.next
            head.next = prv
            prv = head
            head = succ
            cnt-=1
        return prv