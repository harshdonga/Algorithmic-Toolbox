def fib(n):
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    print(f[-1])

if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        fib(n)