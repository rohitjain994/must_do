def findlca(root, lca, x, y):
     
    # base case 1: return false if the tree is empty
    if root is None:
        return False, lca
 
    # base case 2: return true if either `x` or `y` is found
    # with lca set to the current node
    if root == x or root == y:
        return True, root
 
    # recursively check if `x` or `y` exists in the left subtree
    left, lca = findlca(root.left, lca, x, y)
 
    # recursively check if `x` or `y` exists in the right subtree
    right, lca = findlca(root.right, lca, x, y)
 
    # if `x` is found in one subtree and `y` is found in the other subtree,
    # update lca to the current node
    if left and right:
        lca = root
 
    # return true if `x` or `y` is found in either left or right subtree
    return (left or right), lca