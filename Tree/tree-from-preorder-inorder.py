# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def array_tree(l,r):
            nonlocal precnt
            if l>r:return None
            root_val = preorder[precnt]
            root = TreeNode(root_val)
            precnt+=1
            root.left = array_tree(l,inorder_map[root_val]-1)
            root.right = array_tree(inorder_map[root_val]+1,r)
            return root
        inorder_map = {e:i for i,e in enumerate(inorder)}
        precnt = 0
        return array_tree(0,len(preorder)-1)
        