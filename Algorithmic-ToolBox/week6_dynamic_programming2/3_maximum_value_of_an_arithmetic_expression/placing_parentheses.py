# Uses python3
import numpy

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax(m, M, i, j, operators):
    min_val = 9999
    max_val = -9999
    
    for k in range(i, j):
        a = evalt(m[i][k], m[k+1][j], operators[k])
        b = evalt(m[i][k], M[k+1][j], operators[k])
        c = evalt(M[i][k], m[k+1][j], operators[k])
        d = evalt(M[i][k], M[k+1][j], operators[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def get_maximum_value(dataset):
    operators = dataset[1::2]
    operands = dataset[0::2]
    n = len(operands)
    m = numpy.zeros((n,n))
    M = numpy.zeros((n,n))

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]
    for s in range(1,n):
        for i in range(0,n-s):
            j = i+s
            m[i][j] , M[i][j] = MinMax(m, M, i, j, operators)      

    return int(M[0][n-1])

if __name__ == "__main__":
    print(get_maximum_value(input()))
