def gcd(a, b):
    while b != 0:
        x = a%b
        a,b = b,x
    print(a)

if __name__ == "__main__":
    a, b = map(int, input().split())
    gcd(a, b)
