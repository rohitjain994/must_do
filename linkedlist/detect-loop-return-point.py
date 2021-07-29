# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast,slow=head,head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if slow ==fast:
                t = head
                while t!=slow:
                    t=t.next
                    slow = slow.next
                return t
        return None