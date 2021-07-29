# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        postorder = []
        def dfs(node):
            if not node:
                postorder.append("None")
                return
            dfs(node.left)
            dfs(node.right)
            postorder.append(str(node.val))
        dfs(root)
        return " ".join(postorder)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def dfs(postorder):
            if postorder[-1] == "None":
                postorder.pop()
                return
            node = TreeNode(postorder.pop())
            node.right = dfs(postorder)
            node.left = dfs(postorder)
            return node
        return dfs(data.split())

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans