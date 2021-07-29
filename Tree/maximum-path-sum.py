def findMaxPathSum(node, result=-sys.maxsize):
     
    # base case: empty tree
    if node is None:
        return 0, result
 
    # find maximum path sum "starting" from the left child
    left, result = findMaxPathSum(node.left, result)
 
    # find maximum path sum "starting" from the right child
    right, result = findMaxPathSum(node.right, result)
 
    # Try all possible combinations to get the optimal result
    result = max(result, node.data)
    result = max(result, node.data + left)
    result = max(result, node.data + right)
    result = max(result, node.data + left + right)
 
    # return the maximum path sum "starting" from the given node
    return max(node.data, node.data + max(left, right)), result