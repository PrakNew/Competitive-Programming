def insertion_sort(a):
	n=len(a)
	for j in range(1,n):
		key=a[j]
		i=j-1
		while i>=0 and a[i]>key:
			a[i+1]=a[i]
			i-=1
		a[i+1]=key
l=[4,3,2,1,-5]
insertion_sort(l)
print(l)