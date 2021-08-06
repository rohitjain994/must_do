# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #level == len(list)
        # def dfs(node,lvl):
        #     if node.right:
        #         if len(res)<lvl:
        #             res.append(node.right.val)
        #         dfs(node.right,lvl+1)
        #     if node.left:
        #          if len(res)<lvl:
        #             res.append(node.left.val)
        #          dfs(node.left,lvl+1)
        # res = []
        # if root:
        #     res.append(root.val)
        #     dfs(root,2)
        # return res
        def rightView(node, level, dict):
            if node is None:
                return
            rightView(node.left, level + 1, dict)
            rightView(node.right, level + 1, dict)
            dict[level] = node.val
        res = {}
        rightView(root,0,res)
        # print(res)
        return [ res[i] for i in sorted(res) ]