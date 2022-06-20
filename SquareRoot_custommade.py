def mySqrt(x: int) -> int:
    if(x==0):
        return 0
    k = 0
    b = x//2 + 1
    while(b>0):
        while(k+b<=x and (k+b)*(k+b)<=x):
            k+=b
        b = b//2
    return k

print(mySqrt(17))