def isIdentical(x, y):
     
    # if both trees are empty, return true
    if x is None and y is None:
        return True
 
    # if both trees are non-empty and the value of their root node matches,
    # recur for their left and right subtree
    return (x and y) and (x.key == y.key) and \
        isIdentical(x.left, y.left) and isIdentical(x.right, y.right)