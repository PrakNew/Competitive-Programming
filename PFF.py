import math
def seive(n):
	k=[True]*(n+1)
	for x in range(2,int(math.sqrt(n))+1):
		if k[x]:
			for y in range(x*2,n+1,x):
				k[y]=False
	l=[]
	for x in range(2,n+1):
		if k[x]:
			l.append(x)
	return l
def PFF(j):
	r=seive(int(math.sqrt(j)))
	k=[]
	for x in r:
		if j%x==0:
			k.append(x)
	return k
def calc(j):
	r=PFF(j)
	d={}
	for x in r:
		c=0
		while True:
			if j%x!=0:
				break
			c=c+1
			j=j//x
		d[x]=c
	return d
print(calc(616))
