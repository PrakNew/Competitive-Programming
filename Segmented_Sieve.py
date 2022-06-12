import math
def segemented(a,b):
    def seive(n):
        k=[True]*(n+1)
        l=[]
        for i in range(2,int(math.sqrt(n))+1):
            if k[i]:
                for j in range(i*2,n+1,i):
                    k[j]=False
        for x in range(2,n+1):
            if k[x]:
                l.append(x)
        return l

    #print(seive(17))
    
    r=seive(int(math.sqrt(b)))
    #print(r)
    q=[True]*(b-a+1)

    for x in r:
        qw=a//x
        qwe=x*qw
        if qwe<a:
            qwe=qwe+x
        c=qwe
        if c==x:
            c=c+x
        while c<=b:
            q[c-a]=False
            c=c+x
    final=[]
    for x in range(len(q)):

        if q[x]==True:
            if x+a==1:
                continue
            final.append(x+a)

    return final
a,b=list(map(int,input().rstrip().split()))
print(segemented(a,b))