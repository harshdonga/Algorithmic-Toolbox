def gcd(a, b):
    while b != 0:
        x = a%b
        a,b = b,x
    return a

def lcm(a, b):
    res = gcd(a,b)
    print(int(a*b/res))
if __name__ == '__main__':
    a, b = map(int, input().split())
    lcm(a, b)

