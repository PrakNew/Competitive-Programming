def merge(a,p,q,r):
	n1=q-p+1
	n2=r-q
	#w1=[0]*n1
	#w2=[0]*n2
	w1=a[p:q+1]#------------optimized solution for python
	w2=a[q+1:r+1]#-----------optimized solution for python#slicing

	'''for x in range(n1):
		w1[x]=a[p+x]
	for x in range(n2):
		w2[x]=a[q+1+x]'''
	print(w1,w2,p,q,r)
	i,j,k=0,0,p
	while i<n1 and j<n2:
		if w1[i]<=w2[j]:
			a[k]=w1[i]
			i=i+1
		else:
			a[k]=w2[j]
			j=j+1
		k=k+1
	while i<n1:
		a[k]=w1[i]
		i=i+1
		k=k+1
	while j<n2:
		a[k]=w2[j]
		j=j+1
		k=k+1

def mergesort(a,p,r):
	if p<r:
		q=((p+r)//2)
		mergesort(a,p,q)
		mergesort(a,q+1,r)
		merge(a,p,q,r)
l=[9,8,7,6]
mergesort(l,0,len(l)-1)
print(l)

