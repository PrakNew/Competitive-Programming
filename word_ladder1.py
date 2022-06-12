def adjacency(a,b):
    c=0
    for x in range(len(a)):
        if a[x]!=b[x]:
            c+=1
    if c==1:
        return True
    else:
        return False
def finding(check,start,end):
    if start in check:
        check.remove(start)
    d=[[start,1]]
    while d!=[]:
        #print(check)
        j=d.pop(0)
        i=0
        while i<len(check):
            x=check[i]
            if adjacency(x,j[0]):
                item=[0,0]
                item[0]=x
                item[1]=j[1]+1
                d.append(item)
                check.remove(x)
                if x==end:
                    return item[1]
            else:
                i+=1
    return 0
check= ["poon","plee","same","poie","plea","plie","poin"]
start="toon"
end="plea"
print(finding(check[:],start,end))
                
