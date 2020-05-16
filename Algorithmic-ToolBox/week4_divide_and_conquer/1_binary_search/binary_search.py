import sys

def binary_search(a, x, l, r):
    if r>=l:
        mid = l + (r-l) //2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            return binary_search(a, x, mid +1, r)
        else:
            return binary_search(a, x, l, mid -1)
    else:
        return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    ans = []
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x, 0, len(a)-1), end=' ')