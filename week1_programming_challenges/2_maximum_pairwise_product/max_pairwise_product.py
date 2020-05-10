# python3


def max_pairwise_product(numbers):
    m = max(numbers)
    numbers.remove(m)
    n = max(numbers)
    max_product = m*n
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
