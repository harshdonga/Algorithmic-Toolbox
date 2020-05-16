##incorrect solution using sum of subsets method ##


import numpy

def partition3(n,arr):
    s = sum(arr)//3
    if s % 3 != 0:
        return 0
    dp_table = numpy.zeros(( n+1, s+1))

    for i in range(n+1):
        dp_table[i][0] = i

    for i in range(n+1):
        for j in range(s+1):
            if arr[i-1] >j:
                dp_table[i][j] = dp_table[i-1][j]
            if arr[i-1] <= j:
                dp_table[i][j] = dp_table[i-1][j] + dp_table[i-1][j-arr[i-1]]
    
    for i in dp_table:
        print(i)
    return dp_table[n][s] 

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(partition3(n, arr))