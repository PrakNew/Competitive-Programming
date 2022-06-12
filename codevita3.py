from collections import defaultdict
a,b=list(map(int,input().split()))
d=defaultdict(list)
from math import factorial
final=[]
for _ in range(b):
	q,w=map(int,input().split())
	final.append(q)
	d[q].append(w)
	d[w].append(q)
k=[0]*a
def bfs(graph, start,k):
    visited, queue = set(), [start]
    k[start-1]=1
    c=0
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
        	c+=len(graph[vertex]);visited.add(vertex);k[vertex-1]=1;queue+=graph[vertex]
    return k,visited,c//2
c1=0
for x in range(1,a+1):
	if k[x-1]==0:
		k,t,c=bfs(d,x,k)
		qw=len(t)
		qw1=(qw*(qw-1))//2
		c1+=qw1-c
print(c1)