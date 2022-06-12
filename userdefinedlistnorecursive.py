class Node:
    def __init__(self,initial=None):
        self.value=initial
        self.next=None
        return
    def isempty(self):
        if self.value==None:
            return True
        else:
            return False
    def append(self,v):
        if self.isempty():
            self.value=v
            return
        else:
            temp=self
            newnode=Node(v)
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            return
    def insert(self,v):
        if self.isempty():
            self.value=v
            return  
        newnode=Node(v)
        #temp=self
        self.value,newnode.value=newnode.value,self.value
        newnode.next=self.next
        self.next=newnode
        return
    def delete(self,x):
        if self.isempty():
            return
        temp=self
        if self.value==x:
            if self.next==None:
                self.value=None
                return
            self.value=self.next.value
            self.next=self.next.next
        else:
            while temp.next!=None:
                if temp.next.value==x:
                    temp.next=temp.next.next
                    return
                else:
                    temp=temp.next
            return
    def __str__(self):
        selflist = []
        if self.value == None:
            return(str(selflist))

        temp = self
        selflist.append(temp.value)
        
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return(str(selflist))
    def display(self):
        t=self
        while t.next!=None:
            print(t.value,"---->",end=" ")
            t=t.next
        return

j=Node(5)
print(j)
j.append(8)
print(j)
j.insert(8)
print(j)
j.delete(5)
print(j)
j.delete(8)
j.delete(8)
print(j)
j.delete(8)
print(j)
for x in range(10):
    j.append(x)
print(j)
j.delete(5)
j.delete(8)
j.insert(12)
j.append(16)
print(j)
j.display()