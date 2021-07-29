
# Helper function to find minimum value node in a given BST
def findMinimum(root):
 
    while root.left:
        root = root.left
    return root
 
 
def findSuccessor(root, succ, key):
     
    # base case
    if root is None:
        return None
 
    # if a node with the desired value is found, the successor is the minimum value
    # node in its right subtree (if any)
    if root.data == key:
        if root.right:
            return findMinimum(root.right)
 
    # if the given key is less than the root node, recur for the left subtree
    elif key < root.data:
 
        # update successor to the current node before recursing in the left subtree
        succ = root
        return findSuccessor(root.left, succ, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        return findSuccessor(root.right, succ, key)
 
    return succ