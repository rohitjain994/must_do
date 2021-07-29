# Recursive function to check if a given binary tree is height-balanced or not
def isHeightBalanced(root, isBalanced=True):
 
    # base case: tree is empty or not balanced
    if root is None or not isBalanced:
        return 0, isBalanced
 
    # get the height of the left subtree
    left_height, isBalanced = isHeightBalanced(root.left, isBalanced)
 
    # get the height of the right subtree
    right_height, isBalanced = isHeightBalanced(root.right, isBalanced)
 
    # tree is unbalanced if the absolute difference between the height of
    # its left and right subtree is more than 1
    if abs(left_height - right_height) > 1:
        isBalanced = False
 
    # return height of subtree rooted at the current node
    return max(left_height, right_height) + 1, isBalanced