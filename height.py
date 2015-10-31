class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

#function calculate height of the Tree
def height(root):
	if root == None:
		return 0

	leftheight = height(root.left)
	rightheight = height(root.right)

	if (leftheight > rightheight):
		return leftheight + 1
	else:
		return rightheight + 1

if __name__ == '__main__':
	t = Tree(5)
	t.left = Tree(10)
	t.right = Tree(15)
	t.left.right = Tree(10)
	t.left.right.right = Tree(20)

	print "Heigh of the tree ", height(t)