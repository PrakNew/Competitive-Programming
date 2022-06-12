
modulo=10**9+7
def pow (a,b):
    ans = 1
    while(b!=0):
        if((b&1) == 1):
            ans *= a
            ans %= modulo
        a *= a
        a %= modulo
        b>>=1
    return ans
 
def InverseEuler(n):
    return pow(n,modulo-2)
 
def nCr(n,r):
    return (fact[n]*((ifact[r] * ifact[n-r]) % modulo)) % modulo
 
    # calculation of factorials from 1 to number with modulo
def factorial_of_n(number):
    fact=[1]*(number)
    for i in range(1,number):
        fact[i]=(i*fact[i-1])%modulo
    return fact
 
def ifactorial_of_n(number):
    ifact=[1]*(number)
    ifact[-1]=InverseEuler(fact[-1])
    for i in range(number-2,-1,-1):
        ifact[i]=(ifact[i+1]*(1+i))%modulo
    return ifact
N=5*(10**5)+1
fact=factorial_of_n(N)
ifact=ifactorial_of_n(N)
print(nCr(7,2))