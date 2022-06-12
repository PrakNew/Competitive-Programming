from collections import defaultdict
d=defaultdict(dict)
n,e=list(map(int,input().split()))
def floyd_warshall(vertex, adjacency_matrix):
    for k in range(0, vertex):
        for i in range(0, vertex):
            for j in range(0, vertex):
                adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])

for _ in range(e):
    a,b,c=list(map(int,input().split()))
    d[a][b]=c
inf=10000000000000
k=[[0]*n for _ in range(n)]
for x in range(1,n+1):
    for y in range(1,n+1):
        if x==y:
            continue
        q=d[x]
        if y in q:
            k[x-1][y-1]=d[x][y]
        else:
            k[x-1][y-1]=inf
floyd_warshall(n,k)

for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    q=k[a-1][b-1]
    if q==inf:
        print(-1)
    else:
        print(q)
