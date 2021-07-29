def printAncestors(root, node):
     
    # base case
    if root is None:
        return False
 
    # return true if a given node is found
    if root.data == node:
        return True
 
    # search node in the left subtree
    left = printAncestors(root.left, node)
 
    # search node in the right subtree
    right = False
    if not left:
        right = printAncestors(root.right, node)
 
    # if the given node is found in either left or right subtree,
    # the current node is an ancestor of a given node
    if left or right:
        print(root.data, end=' ')
 
    # return true if a node is found
    return left or right