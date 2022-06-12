wt=[1,2,3,2,2]
val=[8,4,0,5,3]
d=dict(zip(wt,val))
k=4
j=5
def knapsack1(d,k,j1):#dictionary is given
	wt=list(d.keys())
	l=[[0]*(k+1) for _ in range(j1+1)]
	for i in range(j1+1):
		for j in range(k+1):
			if j==0 or i==0:
				pass
			elif j<wt[i-1]:
				l[i][j]=l[i-1][j]
			else:
				l[i][j]=max(d[wt[i-1]]+l[i-1][j-wt[i-1]],l[i-1][j])
	return l[j1][k]
def knapsack(wt,val,k,j1):#wt values are seperately given
	l=[[0]*(k+1) for _ in range(j1+1)]
	for i in range(j1+1):
		for j in range(k+1):
			if j==0 or i==0:
				pass
			elif j<wt[i-1]:
				l[i][j]=l[i-1][j]
			else:
				l[i][j]=max(val[i-1]+l[i-1][j-wt[i-1]],l[i-1][j])
	return l[j1][k]
print(knapsack(wt,val,k,j))				