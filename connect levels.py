import Queue

class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.nextRight = None

#function to connect the nodes at the same level
def connectleves(root):
	if root:
		queue = Queue.Queue()

		level = 0
		queue.put([root, level])

		levelhash = {}

		while (queue.qsize() > 0):
			root, level = queue.get()

			level += 1
			children = []

			if level in levelhash:
				children = levelhash[level]

			if root.left:
				children.append(root.left)
				queue.put([root.left, level])

			if root.right:
				children.append(root.right)
				queue.put([root.right, level])

			levelhash[level] = children

		for level in levelhash:
			children = levelhash[level]

			i = 0
			while (i <= len(children)-2):
				children[i].nextRight = children[i+1]
				i += 1



def printlevels(root):
	if root:
		left = printlevels(root.left)
		right = printlevels(root.right)

		if left:
			if left.nextRight:
				print left.data, " => ", left.nextRight.data

		if right:
			if right.nextRight:
				print right.data, " => ", right.nextRight.data

		return root


def inorder(root):
	if root:
		inorder(root.left)
		print root.data,
		inorder(root.right)

if __name__ == '__main__':
	t = Tree(1)

	t.left = Tree(2)
	t.right = Tree(3)

	t.left.left = Tree(4)
	t.left.right = Tree(5)

	t.right.left = Tree(6)
	t.right.right = Tree(7)

	connectleves(t)

	print "Checking whether the links are connected "
	printlevels(t)






