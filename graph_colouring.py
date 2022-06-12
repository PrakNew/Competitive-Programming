from collections import defaultdict
d=defaultdict(list)
j=set()
n=int(input("enter the number of edges"))
for x in range(n):
	a,b=list(map(str,input().split()))
	d[a].append(b)
	d[b].append(a)
	j.add(a)
	j.add(b)
k=defaultdict(int)
def check(a,b):
	k1=d[a]
	#print(a,k1)
	for x in k1:
		#print(k[x],b,x)
		if k[x]==b:
			return False

	return True
for x in j:
	for y in range(1,10):
		if check(x,y):
			k[x]=y
			break
print(k)
