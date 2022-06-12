class Trie:
    def __init__(self):
        self.c=0
        self.arr=[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
root=Trie()
for x in range(int(input())):
    a,b=list(map(str,input().split()))
    if a=="add":
        itr=root
        for x in b:
            j=ord(x)-97
            if itr.arr[j]==None:
                p=Trie()
                itr.arr[j]=p
            itr=itr.arr[j]
            itr.c+=1
    else:
        itr=root
        ans=0
        for x in b:
            j=ord(x)-97
            if itr.arr[j]==None:
                break
            else:
                itr=itr.arr[j]
        else:
            ans=itr.c
        print(ans)
