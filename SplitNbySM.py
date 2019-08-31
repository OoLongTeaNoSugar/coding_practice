# -*- coding:utf-8 -*-
##############
def isPrim(n):
    """
    :param n: 判读一个数是否为质数
    :return:
    """
    if n < 2:
        return False
    max_ = math.sqrt(n)
    i = 2
    while i <= max_:
        if n % i == 0:
            return False
        i += 1
    return True

def divsSumAndCount(n):
    """
    :param n: 请保证n不是质数
    :return: 0) 所有因子的和，但是因子不包括1
	         1) 所有因子的个数，但是因子不包括1
    """
    sums = 0
    count = 0
    for i in range(2, n+1):
        while n % i == 0:
            sums += i
            count += 1
            n /= i
    return [sums, count]


def MinOps(n):
    if n < 2:
        return 0
    if isPrim(n):
        return n - 1
    divsumandcount = divsSumAndCount(n)
    return divsumandcount[0] - divsumandcount[1]


if __name__ == "__main__":
    import math

    for n in range(3, 10):
        print(MinOps(n))
