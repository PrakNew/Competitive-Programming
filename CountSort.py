from itertools import accumulate
def countsort(a,b,k):
	c=[0]*(k+1)
	for x in a:
		c[x]+=1
	print(c)
	c=list(accumulate(c))
	print(c)
	for i in range(len(a)-1,-1,-1):
		b[c[a[i]]]=a[i]
		c[a[i]]-=1
		#print(b)
	print(b)
l=[2,3,1]
b=[0]*(len(l)+1)
#----we will get 1 zero extra at the 0th index
countsort(l,b,max(l))
