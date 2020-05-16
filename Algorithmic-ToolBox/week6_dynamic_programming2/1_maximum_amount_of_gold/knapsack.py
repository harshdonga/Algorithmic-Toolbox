# Uses python3
import sys
import numpy
def optimal_weight(W,n,w):
    dp_table = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            dp_table[i][j] = dp_table[i][j-1]
            if w[j-1]<=i:
                temp = dp_table[i-w[j-1]][j-1] + w[j-1]
                if temp > dp_table[i][j]:
                    dp_table[i][j] = temp

    return int(dp_table[W][n])
if __name__ == '__main__':
    W, n= list(map(int, input().split()))
    w = [int(x) for x in input().split()]
    print(optimal_weight(W,n,w))
