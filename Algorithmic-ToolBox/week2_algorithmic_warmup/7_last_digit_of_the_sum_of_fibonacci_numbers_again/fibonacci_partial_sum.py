m, n = [int(i) for i in input().split()]

if n<=1:
    print(n)  
    exit()
ln = (n+2)%60
lm = (m+1)%60
def fibo(n):
    a,b = 0, 1
    for i in range(2,n+1):
        c = a+b
        c = c%10
        b, a = c, b
    return (c-1)
if ln<=1:
    a = ln-1
else:
    a = fibo(ln)
if lm<=1:
    b = lm-1
else:
    b = fibo(lm)
if a>=b:
    print(a-b)
else:
    print(10+a-b)