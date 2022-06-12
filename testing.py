
def calc(s):
	d={'1': ['0', '1', '2', '3', '4', '5', '6', '7', '8'], '2': ['0', '1', '2', '3', '4'], '3': ['0', '1', '2', '3', '4', '5'], '4': ['0', '1', '2', '3', '4', '5', '6'], '5': ['0', '1', '2', '3', '4', '5', '6', '7'], '6': ['0', '1', '2', '3', '4', '5', '6', '7'], '7': ['0', '1', '2', '3', '4', '5', '6', '7'], '8': ['0', '1', '2', '3', '4', '5', '6', '7'], '9': ['0', '1', '2', '3', '4', '5', '6', '7']}
	s=str(s)
	p=int(s)
	p=str(s)
	if len(p)<len(s):
		s=p
	l=list(s)
	flag=0
	if len(l)==1:
		print(int(s))
		return int(s)
	print(l)
	for x in range(len(l)-1):
		q=l[x]
		w=l[x+1]
		if w in d[q]:
			l[x]=str(int(l[x])-1)
			z=["9"]*(len(l)-x-1)
			l=l[:x+1]+z
			flag=1
			break
	if flag==1:
		j="".join(l)
		j=int(j)
		calc(j)
	else:
		c=1
		for x in l:
			c=c*int(x)
		print(c)
		return c

r=calc(int(input()))



