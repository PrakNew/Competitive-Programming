# here we are finding minimum number of coins needed in order to 
# make a particular sum n with coins in list l
def calculate(n,l):
	m=len(l)
	l.sort()
	p=[[0]+[0]*n for _ in range(m)]
	for x in range(1,n+1):
		if x%l[0]==0:
			p[0][x]=x//l[0]
	for x in range(1,m):
		t=l[x]
		for y in range(1,n+1):
			if y<t:
				p[x][y]=p[x-1][y]
			else:
				p[x][y]=min(p[x-1][y],1+p[x][y-t])
	for x in p:
		print(*x)
calculate(10,[1,5,6,9])