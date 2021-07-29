# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        prv = None
        while head:
            succ = head.next
            head.next = prv
            prv = head
            head = succ
        return prv
        