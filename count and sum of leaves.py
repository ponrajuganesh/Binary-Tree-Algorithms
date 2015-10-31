class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# count the number of leaf nodes
def countleaf(root):
	if root:
		if root.left == None and root.right == None:
			return 1
		else:
			return countleaf(root.left) + countleaf(root.right)
	else:
		return 0

# sum of the leaf nodes
def leafsum(root):
	if root:
		if root.left == None and root.right == None:
			return root.data
		else:
			return leafsum(root.left) + leafsum(root.right)
	else:
		return 0
if __name__ == '__main__':
	t = Tree(5)
	t.left = Tree(1)
	t.right = Tree(15)
	t.left.right = Tree(10)
	t.left.right.right = Tree(20)

	print "Number of leaf Nodes ", countleaf(t)

	print "Sum of leaf Nodes ", leafsum(t)