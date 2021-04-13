def prime_nums(n):
    for i in range(1, n+1):
        if check_num(i):
            print(i)


def check_num(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


prime_nums(120)

