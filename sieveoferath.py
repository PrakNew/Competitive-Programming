'''from math import sqrt
def primerange(n):
	k=[True]*(n+1)
	for x in range(2,int(sqrt(n))+1):
		if k[x]:
			for y in range(x*x,n,x):
				k[y]=False
	g=[]
	for x in range(2,n):
		if k[x]:
			g.append(x)
	print(g)
primerange(18)'''
