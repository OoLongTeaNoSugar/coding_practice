# -*- coding:utf-8 -*-
"""
链接：https://www.nowcoder.com/questionTerminal/bf877f837467488692be703735db84e6
来源：牛客网

牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。
"""

def bag_count(i, v, w):
    if sum(v[:i+1]) <= w:
        return 2 ** (i+1)

    if w <= 0:
        return 0

    if i == 0 and v[i] <= w:
        return 2
    if i == 0 and v[i] > w:
        return 1

    return bag_count(i-1, v[:i], w) + bag_count(i-1, v[:i], w - v[i])

if __name__ == "__main__":
    import sys
    # lines = sys.stdin.readlines()
    n, w = map(int, sys.stdin.readline().split())
    v = map(int, sys.stdin.readline().split())
    v = sorted(v)
    print(bag_count(n-1, v, w))

