class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


#returns mirror of the Tree
def mirror(root):
	if root == None:
		return None

	left = mirror(root.left)
	right = mirror(root.right)

	temp = root.right
	root.right = left
	root.left = temp

	return root

#printing the tree
def inorder(root):
	if root:
		inorder(root.left)
		print root.data,
		inorder(root.right)

if __name__ == '__main__':
	t = Tree(5)
	t.left = Tree(1)
	t.right = Tree(15)
	t.left.right = Tree(10)
	t.left.right.right = Tree(20)

	print "Actual Tree ", inorder(t)

	print "Mirror Tree ", inorder(mirror(t))
