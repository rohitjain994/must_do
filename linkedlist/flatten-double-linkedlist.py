"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        stack = []
        temp = Node(0,None,head,None)
        stack.append(head)
        prev = temp
        while stack:
            node = stack.pop()
            node.prev = prev
            prev.next = node
            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
            prev = node
        temp.next.prev = None
        return temp.next
        