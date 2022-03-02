from math import sqrt
def find_median(n_num):
    n = len(n_num)
    n_num = sorted(n_num)
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n_num[n//2]
    return median


def math_spread(numbers):
    n = len(numbers)
    x2 = sum(numbers)/n
    s = 0
    for i in range(n):
        s += (numbers[i] - x2)**2
    D = (1/(n-1))*s
    sigma = sqrt(D)
    print(sigma)
    numbers = sorted(numbers)
    numbers_1 = numbers[:n//2]
    numbers_2 = numbers[n//2:]
    
    N_1 = find_median(numbers_1)
    N_2 = find_median(numbers_2)
    print(N_2 - N_1)

math_spread([29, 36, 49, 59, 70, 71, 87, 88])