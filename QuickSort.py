def partition(a,p,r):
	key=a[r]
	i=p-1
	for j in range(p,r):
		if a[j]<=key:
			i+=1
			a[i],a[j]=a[j],a[i]
	a[i+1],a[r]=a[r],a[i+1]
	return i+1
def quicksort(a,p,r):
	if p<r:
		q=partition(a,p,r)
		quicksort(a,p,q-1)
		quicksort(a,q+1,r)
p=[4,3,2,1,8,3,4]
quicksort(p,0,len(p)-1)
print(p)
