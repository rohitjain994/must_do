def isBST(node, minKey, maxKey):
     
    # base case
    if node is None:
        return True
 
    # if the node's value falls outside the valid range
    if node.data < minKey or node.data > maxKey:
        return False
 
    # recursively check left and right subtrees with an updated range
    return isBST(node.left, minKey, node.data) and \
        isBST(node.right, node.data, maxKey)