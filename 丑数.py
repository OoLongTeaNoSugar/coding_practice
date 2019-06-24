# -*- coding:utf-8 -*-
"""
Q: 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。
求按从小到大的顺序的第N个丑数。

A: 建立一个长度为n的数组保存N个丑数，
在这N个数中，某个位置要求的丑数一定是前面某个丑数乘以2、3或者5得到的结果。
分别记录乘以2能得到的最大丑数M2, 乘以3以后能得到的最大丑数M3, 乘以5以后能得到的最大丑数M5.
那么下一个丑数一定是这三个最大丑数中最小的那个。
因为是按照顺序存放的丑数，所以对于乘以2来说，肯定存在一个丑数T2,
 排在它之前的每一个丑数乘以2得到的结果都会小于已有的最大丑数，记住该丑数的位置，
 每次生成新的丑数时，更新它。对于乘以3或者5，同理
"""
class Solution:
    def GetUglyNumber(self, index):
        # write code here
        if not index:
            return 0

        # 建立一个数组按顺序储存丑数
        res = [1] * index

        # 记录目前最大的M2，M3，M5
        index2 = 0
        index3 = 0
        index5 = 0

        # 由于1是丑数，故从第二位开始操作
        ugly_index = 1
        while ugly_index < index:
            Minvalue = min(res[index2] * 2, res[index3] * 3, res[index5] * 5)
            res[ugly_index] = Minvalue

            # 判断minvalue 是M2,M3,M5？
            while res[index2] * 2 <= Minvalue:
                index2 += 1
            while res[index3] * 3 <= Minvalue:
                index3 += 1
            while res[index5] * 5 <= Minvalue:
                index5 += 1

            ugly_index += 1

        return res[-1]

