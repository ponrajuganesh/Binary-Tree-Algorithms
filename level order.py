import Queue

class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

#level order traversal in the tree using Queue
def printlevelorder(root):

	queue = Queue.Queue()

	queue.put(root)

	while (queue.qsize() > 0):
		node = queue.get()

		print node.data,

		if (node.left):
			queue.put(node.left)

		if (node.right):
			queue.put(node.right)

#returns height of the tree
def height(root):
	if root:
		lheight = height(root.left)
		rheight = height(root.right)

		if (lheight > rheight):
			return lheight + 1
		else:
			return rheight + 1
	else:
		return 0

#prints the nodes as every level at one line using printUtil and printlevel
def printUtil(root):

	for i in range(1, height(root)+1):
		printlevel(root, i)
		print "\n"

def printlevel(root, level):
	if root:
		if level == 1:
			print root.data,
		elif level > 1:
			printlevel(root.left, level-1)
			printlevel(root.right, level-1)


if __name__ == '__main__':
	t = Tree(5)
	t.left = Tree(1)
	t.right = Tree(15)
	t.left.right = Tree(10)
	t.left.right.right = Tree(20)

	print "Level Order traversal ", printlevelorder(t)

	print "Level Order traversal each level at a line "
	printUtil(t)