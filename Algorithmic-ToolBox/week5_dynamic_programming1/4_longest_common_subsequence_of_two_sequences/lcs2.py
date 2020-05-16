#Uses python3
import sys
import numpy

def lcs2(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp_table = numpy.zeros((n1+1 , n2+1))
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1] + 1
            if s1[i-1] != s2[j-1]:
                dp_table[i][j] = max(dp_table[i][j-1], dp_table[i-1][j])
    
    return int(dp_table[n1][n2])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))