# we are provided with a list which contains what are the coin values 
# and we are provided with n i.e the value of the sum we want
def calculate(n,l):
	m=len(l)
	l.sort()
	p=[[1]+[0]*n for _ in range(m)]
	for x in range(1,n+1):
		if x%l[0]==0:
			p[0][x]=1
	for x in range(1,m):
		t=l[x]
		for y in range(1,n+1):
			if y<t:
				p[x][y]=p[x-1][y]
			else:
				p[x][y]=p[x-1][y]+p[x][y-t]
	for x in p:
		print(*x)
calculate(5,[2,3])