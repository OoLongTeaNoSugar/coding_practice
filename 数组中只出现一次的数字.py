# -*- coding:utf-8 -*-
"""
Q: 一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。

"""
class Solution:
    def FindNumsApearOnce(self, array):
        hashmap = {}
        for i in array:
            if str(i) in hashmap:
                hashmap[str(i)] += 1
            else:
                hashmap[str(i)] = 1

        res = []
        for k in hashmap.keys():
            if hashmap[k] == 1:
                res.append(int(k))
        return res
