def previous(s):
    i=len(s)-1
    s=list(s)
    while i>0 and s[i]>=s[i-1]:
        i-=1
    if i<=0:
        return "NO"
    j=i-1
    while j<len(s)-1 and s[j+1]<s[i-1]:
        j+=1
    s[j],s[i-1]=s[i-1],s[j]
    s=s[:i]+s[i:][::-1]
    k="".join(s)
    return k
def next(s):
    i=len(s)-1
    s=list(s)
    while i>0 and s[i]<=s[i-1]:
        i=i-1
    if i<=0:
        return "NO"
    p=i-1
    s=s[:i]+s[i:][::-1]
    j=p
    while j<len(s) and s[j]<=s[p]:
        j+=1
    s[p],s[j]=s[j],s[p]
    k="".join(s)
    return k
r="01255330"
a=previous(r)
b=next(a)
print(a,b,r)
if b==r:
    print("yes")
else:
    print("NO")

