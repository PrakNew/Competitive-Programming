class tree:
	def __init__(self,inv=None):
		self.data=inv
		self.left=None
		self.right=None
	def isempty(self):
		if self.data==None:
			return True
		else:
			return False
	def insert(self,value):
		if self.isempty():
			self.data=value
		else:
			if value>self.data:
				if self.right==None:
					temp=tree(value)
					self.right=temp
				else:
					self.right.insert(value)
			else:
				if self.left==None:
					temp=tree(value)
					self.left=temp
				else:
					self.left.insert(value)
	def display_nodes(root):
	    if root is None:
	        return

	    if root.left is not None:
	        root.left.display_nodes()

	    print(root.data, end=' ')

	    if root.right is not None:
	        root.right.display_nodes()
t=tree(5)
t.insert(4)
t.insert(6)
t.insert(5)
t.insert(-1)
t.display_nodes()