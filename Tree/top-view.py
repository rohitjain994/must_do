def printTop(root, dist, level, dict):
     
    # base case: empty tree
    if root is None:
        return
 
    # if the current level is less than the maximum level seen so far
    # for the same horizontal distance, or if the horizontal distance
    # is seen for the first time, update the dictionary
    if dist not in dict or level < dict[dist][1]:
        # update value and level for current distance
        dict[dist] = (root.key, level)
 
    # recur for the left subtree by decreasing horizontal distance and
    # increasing level by 1
    printTop(root.left, dist - 1, level + 1, dict)
 
    # recur for the right subtree by increasing both level and
    # horizontal distance by 1
    printTop(root.right, dist + 1, level + 1, dict)