def printVertical(node, dist, dict):
     
    # base case: empty tree
    if node is None:
        return
 
    # insert nodes present at a current horizontal distance into the dictionary
    dict.setdefault(dist, []).append(node.key)
 
    # recur for the left subtree by decreasing horizontal distance by 1
    printVertical(node.left, dist - 1, dict)
 
    # recur for the right subtree by increasing horizontal distance by 1
    printVertical(node.right, dist + 1, dict)