
def find(s):
    t=s
    l=0
    r=0
    z=[0]*len(t)
    for i in range(len(t)):
        if(i>r):
            l=r=i
            while(r<len(t) and t[r]==t[r-l]):
                r+=1
            z[i]=r-l
            r-=1
        else:
            i1=i-l
            if(z[i1]<r-i+1):
                z[i]=z[i1]
            else:
                l=i
                while(r<len(t) and t[r]==t[r-l]):
                    r+=1
                z[i]=r-l
                r-=1
    print(z)
    return sum(z)+len(s)
    
for i in range(int(input())):
    s=input()
    print(find(s))
    
