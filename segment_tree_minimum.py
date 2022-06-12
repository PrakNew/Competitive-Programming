def construct(inp,segtree,low,high,pos):
	if low==high:
		segtree[pos]=inp[low]
		#print(segtree)
		return
	mid=(low+high)//2
	construct(inp,segtree,low,mid,2*pos+1)
	construct(inp,segtree,mid+1,high,2*pos+2)
	segtree[pos]=min(segtree[2*pos+1],segtree[2*pos+2])
def rangemin(segtree,qlow,qhigh,low,high,pos):
	if qlow<=low and qhigh>=high:#total overlap
		return segtree[pos]
	if qlow>high or qhigh<low:
		return 9999999999
	mid=(low+high)//2
	return min(rangemin(segtree,qlow,qhigh,low,mid,2*pos+1),rangemin(segtree,qlow,qhigh,mid+1,high,2*pos+2))


a=[-1,2,4,0]
b=[999999999999]*7
#print(b)
construct(a,b,0,3,0)
print(b)
print(rangemin(b,0,3,0,3,0))