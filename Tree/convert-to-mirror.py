def convertToMirror(root):
     
    # base case: if the tree is empty
    if root is None:
        return
 
    # convert left subtree
    convertToMirror(root.left)
 
    # convert right subtree
    convertToMirror(root.right)
    # swap
    root.left,root.right = root.right,root.left