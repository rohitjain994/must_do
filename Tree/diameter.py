def getDiameter(root, diameter):
     
    # base case: tree is empty
    if root is None:
        return 0, diameter
 
    # get heights of left and right subtrees
    left_height, diameter = getDiameter(root.left, diameter)
    right_height, diameter = getDiameter(root.right, diameter)
 
    # calculate diameter "through" the current node
    max_diameter = left_height + right_height + 1
 
    # update maximum diameter (note that diameter "excluding" the current
    # node in the subtree rooted at the current node is already updated
    # since we are doing postorder traversal)
    diameter = max(diameter, max_diameter)
 
    # it is important to return the height of the subtree rooted at the current node
    return max(left_height, right_height) + 1, diameter