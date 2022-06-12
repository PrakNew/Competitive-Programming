def result(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000
    assert(0 <= num)
    if (num < 20):
        return d[num]
    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + d[num % 10]
    if (num < k):#1000
        if num % 100 == 0: return d[num // 100] + 'hundred'
        else: return d[num // 100] + 'hundred' + result(num % 100)
    if (num < m):
        if num % k == 0: return result(num // k) + 'thousand'
        else: return result(num // k) + 'thousand' + result(num % k)
    if (num < b):
        if (num % m) == 0: return result(num // m) + 'million'
        else: return result(num // m) + 'million' + result(num % m)
    if (num < t):
        if (num % b) == 0: return result(num // b) + 'billion'
        else: return result(num // b) + 'billion' + result(num % b)
    if (num % t == 0): return result(num // t) + ' trillion'
    else: return result(num // t) + 'trillion' + result(num % t)
#print(result(99999))
a,b=list(map(int,input().rstrip().split()))
a,b=min(a,b),max(a,b)
#print(a,b)
while True:
	if a==b:
		print(a)
		break
	if a>99999 or b>99999 or a+b>99999:
		print("Out of bounds")
		break
	q=result(a)
	w=result(b)
	if w<q:
		print(a+b)
		break
	else:
		a=a+a
		b=b+b
