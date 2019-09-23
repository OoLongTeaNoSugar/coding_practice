# -*- coding:utf-8 -*-
# ####################
"""
a-z 子序列按照字典序组织，比如a(1)....z(26) ab(27) .... az(51)...
给定子序列，返回序号
"""

def g(i, lenth):
    """
    :param i:
    :param lenth:
    :return: 以i号字符开头的长度为lenth的子序列有几个
    """
    sums = 0
    if lenth == 1:
        return 1
    for j in range(i + 1, 27):
        sums += g(j, lenth - 1)
    return sums

def f(n):
    """
    长度为n的子序列有几个
    :param n:
    :return:
    """
    sums = 0
    for i in range(1, 27):
        sums += g(i, n)
    return sums

def Kth(s):
    """
    返回该子序列的序号
    :param s:
    :return:
    """
    sums = 0
    lenth  = len(s)
    for i in range(1, lenth):
        sums += f(i)
    first = ord(s[0]) - ord('a') + 1
    for i in range(1, first):
        sums += g(i, lenth)
    pre = first
    for i in range(1, lenth):
        cur = ord(s[i]) - ord('a') + 1
        for j in range(pre + 1, cur):
            sums += g(j, lenth - 1)
        pre = cur

    return sums + 1

if __name__ == "__main__":
    test1 = 'a'
    test2 = 'ab'
    test3 = 'abcd'
    print(Kth(test1))
    print(Kth(test2))
    print(Kth(test3 ))