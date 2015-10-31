class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def size(root):
	if root == None:
		return 0
	else:
		return 1 + size(root.left) + size(root.right)

if __name__ == '__main__':
	t = Tree(5)
	t.left = Tree(10)
	t.right = Tree(15)
	t.left.right = Tree(10)

	print "Size of the tree ", size(t)