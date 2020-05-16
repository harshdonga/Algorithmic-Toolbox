import sys
import random


def partition3(a, left, right):
    pivot_value = a[left]
    l = i = left
    e = right
    while i <= e:
        if a[i] < pivot_value:
            a[i], a[l] = a[l], a[i]
            l += 1
            i += 1
        elif a[i] == pivot_value:
            i += 1
        else:
            a[i], a[e] = a[e], a[i]
            e -= 1
        pI = [l, e]
    return pI


def partition2(a, left, right):
    pivot = random.randint(left, right)
    a[right], a[pivot] = a[pivot], a[right]
    pivot_value = a[right]
    pIndex = left
    for i in range(left, right):
        if a[i] <= pivot_value:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex += 1
    a[right], a[pIndex] = a[pIndex], a[right]
    return pIndex


def randomized_quick_sort(a, left, right):
    if left >= right:
        return

    pivot = random.randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]
    pIndex = partition3(a, left, right)
    randomized_quick_sort(a, left, pIndex[0] - 1)
    randomized_quick_sort(a, pIndex[1] + 1, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')