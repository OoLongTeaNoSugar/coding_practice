# -*- coding:utf-8 -*-
##############
# 在机器上有一堆衣服要把他们平均分，需要几轮

def MinOps(arr):
    """
    :param arr: 初始状态数组
    :return: 最少操作轮数,无法完成输出-1
    """
    if not arr or len(arr) == 0:
        return 0
    size = len(arr)
    sums = 0
    for i in range(size):
        sums += arr[i]
    if sums % 2 != 0:
        return -1
    avg = sums / size
    leftSum = 0
    ans = 0
    for i in range(len(arr)):
        L = i * avg -leftSum
        R = (size - i - 1) * avg - (sums - leftSum - arr[i])
        if L > 0 and R > 0:
            ans = max(ans, abs(L) + abs(R))
        else:
            ans = max(ans, max(abs(L), abs(R)))
        leftSum += arr[i]
    return ans
