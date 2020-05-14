#Uses python3

import sys
import numpy
                                    
def lcs3(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    dp_table = numpy.zeros((n1+1 , n2+1, n3+1))
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            for k in range(1, n3+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    dp_table[i][j][k] = dp_table[i-1][j-1][k-1] + 1
                else:
                    dp_table[i][j][k] = max(dp_table[i-1][j][k], dp_table[i][j-1][k], dp_table[i][j][k-1])
    
    return int(dp_table[-1][-1][-1])
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
