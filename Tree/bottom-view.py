def printBottom(root, dist, level, dict):
     
    # base case: empty tree
    if root is None:
        return
 
    # if the current level is more than or equal to the maximum level seen so far
    # for the same horizontal distance or horizontal distance is seen for
    # the first time, update the dictionary
    if dist not in dict or level >= dict[dist][1]:
        # update value and level for the current distance
        dict[dist] = (root.key, level)
 
    # recur for the left subtree by decreasing horizontal distance and
    # increasing level by 1
    printBottom(root.left, dist - 1, level + 1, dict)
 
    # recur for the right subtree by increasing both level and
    # horizontal distance by 1
    printBottom(root.right, dist + 1, level + 1, dict)