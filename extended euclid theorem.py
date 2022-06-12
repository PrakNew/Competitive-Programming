'''a,b,c=list(map(int,input().rstrip().split()))
b=bin(b)[2:]
a1=a
for x in range(1,len(b)):
    if b[x]=="1":
        a1=(a1**2)%c
        a1=(a1*a)%c
    elif b[x]=="0":
        a1=(a1**2)%c
if b=="1":
    a1=a%c
elif b=="0":
    a1=1
print(a1)'''
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

print (egcd(4,5))