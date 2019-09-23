# -*- coding:utf-8 -*-

"""
求最大子数组的异或和
"""
def mostEOR(arr):
    ans = 0
    xor = 0
    mosts = [0 for _ in range(len(arr))]
    dmap = {}
    dmap[0] = 1
    for i in range(len(arr)):
        xor ^= arr[i]
        if xor in dmap:
            pre = dmap[xor]
            mosts[i] = 1 if pre == -1 else (mosts[pre] + 1)
        if i > 0:
            mosts[i] = max(mosts[i - 1], mosts[i])
        dmap[xor] = i
        ans = max(ans, mosts[i])
    return ans
