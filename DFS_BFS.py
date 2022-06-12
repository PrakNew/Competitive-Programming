from collections import defaultdict
d=defaultdict(list)
s=0
l=[]
def BFS(n):
	global s,l
	s=0
	l+=[n]
	q=[]
	while l!=[]:
		p=d[l[0]]
		s+=l[0]
		for x in p:
			if x in q or x in l:
				pass
			else:
				l.append(x)
		print("queue",l)
		q.append(l.pop(0))
		print(q)
	print(s)
def DFS(n):
	global s,l
	s=0
	l+=[n]
	q=[]
	while l!=[]:
		p=d[l[0]]
		s+=l[0]
		q.append(l.pop(0))
		for x in p:
			if x in q or x in l:
				pass
			else:
				l.insert(0,x)
		print("stack",l)
		print(q)
	print(s)

for x in range(int(input())):
	a,b=map(int,input().split())
	d[a].append(b)
	d[b].append(a)
DFS(1)
print()
BFS(1)
graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A')
#-----------------------------------------------Recursion
graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'A', [])
print(visited)

'''input:

8
1 2
1 3
2 4
4 5
4 6
3 7
3 8
2 9
'''