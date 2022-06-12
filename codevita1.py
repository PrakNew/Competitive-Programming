from collections import deque
n=int(input())
l=[]
def find(start,end,main):
  t=end
  t1=start
  l=[]
  p=[]
  fin1=[]
  fin2=[]
  for x in range(t+1):
    if x<t1:
      continue
    l.append((t1,x))
    fin1.append(main[t1][x])
    if x!=t1:
      p.append((x,t1))
      fin2.append(main[x][t1])
  for x in range(t1+1,t+1):
    l.append((x,t))
    fin1.append(main[x][t])
    if x!=t:
      p.append((t,x))
      fin2.append(main[t][x])
  l=l+p[::-1]
  fin1+=fin2[::-1]
  return l,fin1
for _ in range(n):
	l.append(input().split())
qwer1=[]
qwer2=[]
arrange=[]
for x in range(n//2):
	ini=x
	fin=n-x-1
	asd,asdf=find(ini,fin,l)
	qwer1.append(asd)
	ind=asdf.index("X")
	ind1=len(asdf)-ind
	k1=deque(asdf)
	if ind<ind1:
		arrange.append(ind)
		k1.rotate(-ind)
	else:
		arrange.append(-ind1)
		k1.rotate(ind1)
	qwer2.append(list(k1))
print(*arrange)
for x in range(len(qwer1)):
	p=qwer1[x]
	t=qwer2[x]
	for y in range(len(p)):
		p1=p[y]
		l[p1[0]][p1[1]]=t[y]
for x in l:
	print(*x)
