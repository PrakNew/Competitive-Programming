indexing={'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10, 'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24, 'O': 25, 'P': 26, 'Q': 27, 'R': 28, 'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34, 'Y': 35, 'Z': 36}
def convert(data):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM","MMM","MMMM"]
    
    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o =  ones[data % 10]
    
    return t+h+te+o
n = int(raw_input())
while True:
    if 1<=n<=3999:
        n = convert(n)
        #print(n)
        n=n[::-1]
        base = indexing[max(n)]
        temp=0
        for i in range(len(n)-1,-1,-1):
            temp+=(indexing[n[i]]-1)*pow(base,i)
        n=temp
    else:
        print(n)
        break
