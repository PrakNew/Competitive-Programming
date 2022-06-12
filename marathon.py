from collections import defaultdict
from sys import *
n=int(stdin.readline())
k=int(stdin.readline())
if k&1!=0:
	k+=1
l=[]
for _ in range(n):
	l.append(list(map(int,stdin.readline().split())))
d=defaultdict(int)
for x in range(2,k,2):
	q=[]
	for y in range(len(l)):
		p=sum(l[y][:x])*l[y][-1]
		q.append(p)
	#print(q)
	w=max(q)
	for y in range(len(q)):
		if q[y]==w:
			d[y+1]+=1
j=max(d.values())
for x in d:
	if d[x]==j:
		print(x)
		break