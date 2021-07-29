def leftView(root, level, dict):
     
    # base case
    if root is None:
        return
 
    // insert the current node and level information into the map
    dict[level] = root.key
 
    // recur for the right subtree before the left subtree
    leftView(root.right, level + 1, dict)
    leftView(root.left, level + 1, dict)