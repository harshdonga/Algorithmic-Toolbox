def get_change(m):
    arr = [m+1]*(m+1)
    arr[0] = 0
    coins = [1,3,4]
    for i in range(1,len(arr)):
        if i >= coins[0]:
            arr[i] = min(arr[i-coins[0]]+1, arr[i])
        if i >= coins[1]:
            arr[i] = min(arr[i-coins[1]]+1, arr[i])
        if i >= coins[2]:
            arr[i] = min(arr[i-coins[2]]+1, arr[i])
    return arr[-1]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
