# Recursive function to traverse the nodes in a preorder fashion
def leftView(root, level, dict):

	# base case
	if root is None:
		return

	# if the level is visited for the first time, insert the current node
	# and level information into the dictionary
	

	leftView(root.left, level + 1, dict)
	leftView(root.right, level + 1, dict)
	dict[level] = root.key
