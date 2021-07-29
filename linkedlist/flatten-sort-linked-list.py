# A Linked List Node
class Node:
    def __init__(self, data, next=None, down=None):
        self.data = data
        self.next = next
        self.down = down
 
 
# Takes two lists sorted in increasing order and merge their nodes
# to make one big sorted list, which is returned
def sortedMerge(a, b):
 
    # base cases
    if a is None:
        return b
 
    elif b is None:
        return a
 
    # pick either `a` or `b`, and recur
    if a.data <= b.data:
        result = a
        result.down = sortedMerge(a.down, b)
 
    else:
        result = b
        result.down = sortedMerge(a, b.down)
 
    return result
 
 
# Helper function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.down
 
    print("None")
 
 
# Recursive function to flatten and sort a given list
def flatten(head):
 
    # base case: an empty list
    if head is None:
        return head
 
    # Merge this list with the list on the right side
    sorted = sortedMerge(head, flatten(head.next))
 
    # set next link to None after flattening
    head.next = None
 
    return sorted
 
 
# Helper function to build a linked list from elements of a given list
def createVerticalList(head, A):
 
    for key in A:
        head = Node(key, head)
    return head
 
 
if __name__ == '__main__':
 
    first = [8, 6, 4, 1]
    second = [7, 3, 2]
    third = [9, 5]
    fourth = [12, 11, 10]
 
    head = createVerticalList(None, first)
    head.next = createVerticalList(head.next, second)
    head.next.next = createVerticalList(head.next.next, third)
    head.next.next.next = createVerticalList(head.next.next.next, fourth)
 
    # flatten and sort the list
    flatten(head)
 
    # print the flattened and sorted linked list
    printList(head)
 