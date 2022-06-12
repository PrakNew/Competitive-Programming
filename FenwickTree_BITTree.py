def sumq(a,n):
    s=0
    i=n+1
    while i:
        s=s+a[i]
        i-=i&(-i)
    return s
def update(a,i,n,v):
    i+=1
    while i<=n:
        a[i]+=v
        i+=i&(-i)
def construct(a,n):
    b=[0]*(n+1)
    for x in range(n):
        update(b,x,n,a[x])
    return b
a=[3,2,-1,6,5,4,-3,3,7,2,3]
b=construct(a,len(a))
print(b)
print(sumq(b,2))