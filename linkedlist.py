class Node:
	def __init__(self,initval=None):
		self.value=initval
		self.next=None
	def insert(self,key):
		temp=Node(key)
		q=self
		while q.next!=None:
			q=q.next
		q.next=temp
	def insertatbig(self,key):
		n=Node(key)
		k=self
		n.next=self
		self=n
	def delete(self,key):
		temp=self
		a=self
		try:
			while temp.value!=key:
				a=temp
				temp=temp.next
			a.next=temp.next
			temp.next=None
		except:
			print("ELEMENT NOT FOUND")

	def display(self):
		temp=self
		while temp.next!=None:
			print(temp.value,end="---->")
			temp=temp.next
		print(temp.value)
a=Node(5)
a.insert(6)
a.insert(7)
a.display()
a.delete(8)
a.insertatbig(4)
a.display()