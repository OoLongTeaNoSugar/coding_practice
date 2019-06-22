# -*- coding:utf-8 -*-
"""
Q: 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0

A: 第一种思路O(n*lgn)：出现次数超过一半的数字，一定位于数组中间的位置，
找到数组中间位置的数字，然后再顺序检索这个数字的出现次数是否超过一半；
第二种思路O(n)：出现次数超过一半的数，
它的出现次数比其他所有数字出现次数的总和还要多，保存两个值，数组中的数字和它的出现次数。
如果下一个数字等于该数字，那么出现次数加一，如果不相等，次数减一，
当次数为0时，保存下一个数字，并重置出现次数为1，
我们要找的数字就是最后一次把次数重置为1的时候，保存的数字。
最后要检查得到的元素出现次数是否超过一半。
"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        lenth = len(numbers)
        if not numbers:
            return 0
        res = numbers[0]
        times = 1

        for i in range(1, lenth):
            if times == 0:
                res = numbers[i]
                times = 1
            elif numbers[i] == res:
                times += 1
            else:
                times -= 1

        if not self.Check2Times(numbers, lenth, res):
            return 0
        return res

    def Check2Times(self, numbers, lenth, number):
        times = 0
        for i in range(lenth):
            if numbers[i] == number:
                times += 1

        if lenth < times * 2:
            return True
        else:
            return False

