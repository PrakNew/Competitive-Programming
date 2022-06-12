from itertools import combinations
l=[5,10,12,13,15,18]
k=30
p=[]
for i in range(1,len(l)+1):
	p.extend(list(filter(lambda x:sum(x)==k,combinations(l,i))))
print(p)