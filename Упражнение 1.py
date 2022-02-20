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
    
print(find_median([1, 2, 3, 4]))
