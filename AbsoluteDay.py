abd={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",0:"Sunday"}
ye={0:0,1:5,2:3,3:1}
nod={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
d1,d2,d3=list(map(int,input().rstrip().split("/")))
k=d3
d3=str(d3)
a=d3[2:]
b=d3[:2]+"00"
b=int(b)
j1=ye[(b%400)//100]
a=int(a)
a=a-1
#print(a)
j=a//4
#print(j)
j2=(j*2+(a-j))%7
s=0
for x in range(1,d2):
	s+=nod[x]
if k%400==0 or k%4==0 and k%100!=0:
	if d2>2:
		s=s+1
s=s+d1
j3=s%7
fi=(j1+j2+j3)%7
#print(j1,j2,j3,fi)
print(abd[fi])


