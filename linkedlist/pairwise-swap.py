# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(start)
        return head