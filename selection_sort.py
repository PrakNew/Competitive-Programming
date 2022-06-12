def selection_sort(l):
	n=len(l)
	for x in range(n-1):
		key=l[x]
		pos=x
		for y in range(x+1,n):
			if l[y]<key:
				pos=y
				key=l[y]
		l[pos],l[x]=l[x],l[pos]
l=[4,3,2,1,5]
selection_sort(l)
print(l)
