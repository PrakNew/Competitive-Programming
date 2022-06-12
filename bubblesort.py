def bubble_sort(l):
	n=len(l)
	for x in range(n-1):
		for y in range(n-x-1):
			if l[y]>l[y+1]:
				l[y],l[y+1]=l[y+1],l[y]
l=[4,3,2,1 ,0 ,-1 ,-2 ,-3]
bubble_sort(l)
print(l)