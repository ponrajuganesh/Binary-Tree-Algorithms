class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

#sum of Tree
def treesum(root):
	if root == None:
		return 0

	return treesum(root.left) + root.data + treesum(root.right)

if __name__ == '__main__':
	t = Tree(5)
	t.left = Tree(1)
	t.right = Tree(15)
	t.left.right = Tree(10)
	t.left.right.right = Tree(20)

	print "Sum of the tree ", treesum(t)