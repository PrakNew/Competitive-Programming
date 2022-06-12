def search(a,p,r,key):#recursive approach
	if p<=r:
		q=(p+r)//2
		if a[q]==key:
			return q
		elif key<a[q]:
			return search(a,p,q-1,key)
		else:
			return search(a,q+1,r,key)
	else:
		return -1
l=[1,2,3,4,5,6,7,8,9]
print(search(l,0,8,1))