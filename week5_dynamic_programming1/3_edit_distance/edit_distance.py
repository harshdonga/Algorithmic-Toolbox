# # Uses python3
import numpy

def EditDistance(s, t):
    ls, lt = len(s), len(t) 
    dp_table = numpy.zeros((ls+1 , lt+1))
    for i in range(lt+1):
        dp_table[0][i] = i
    for i in range(ls+1):
        dp_table[i][0] = i
    for i in range(1, ls+1):
        for j in range(1, lt+1):
            if s[i-1] == t[j-1]:
                dp_table[i][j] = min((dp_table[i][j-1]+ 1), (dp_table[i-1][j] + 1) , (dp_table[i-1][j-1]))
            if s[i-1] != t[j-1]:
                dp_table[i][j] = min((dp_table[i][j-1]+ 1), (dp_table[i-1][j] + 1) , (dp_table[i-1][j-1] + 1))
    
    return int(dp_table[ls][lt])
if __name__ == '__main__':
    print(EditDistance(input(), input()))