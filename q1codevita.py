
slab =list(map(int,raw_input().rstrip().split()))
tax =list(map(int,raw_input().rstrip().split()))
rebet = int(raw_input())
p_t =list(map(int,raw_input().rstrip().split()))
prak=len(p_t)*rebet
slab_tax=[0]
q=len(slab)
for i in xrange(q-1):
    slab_tax.append(int((slab[i+1]-slab[i])*tax[i]//100))
qwe=len(p_t)
for i in xrange(qwe):
    x = p_t[i]
    g = 0
    for j in xrange(len(slab_tax)):
        if(x >= slab_tax[j]):
            g = slab[j]
            x -= slab_tax[j]
        else:
            p = (x*100)/(tax[j-1])
            g += p
            x=0 
            break
    if(x>0):
        p = (x*100)/(tax[-1])
        g += p
    prak += (g)
print(prak)