n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
p1=set(l1)
p2=set(l2)
r=p1|p2
q=int(input())
for _ in range(q):
	a,b,c,d=map(int,input().split())
	t1=set(l1[a-1:b])|set(l2[c-1:d])
	print(len(r-t1))
	