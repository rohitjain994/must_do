def printDiagonal(node, diagonal, dict):
     
    # base case: empty tree
    if node is None:
        return
 
    # insert the current node into the current diagonal
    dict.setdefault(diagonal, []).append(node.data)
 
    # recur for the left subtree by increasing diagonal by 1
    printDiagonal(node.left, diagonal + 1, dict)
 
    # recur for the right subtree with the same diagonal
    printDiagonal(node.right, diagonal, dict)