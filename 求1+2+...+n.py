# -*- coding:utf-8 -*-
"""
Q: 求1+2+3+…+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

A: 还可以利用python中的and特性，a and b，a为False，返回a，a为True，就返回b

"""
class Solution:
    def Sum_Solution(self, n):
        # write code here
        # 递归，一行搞定
        return n and self.Sum_Solution(n - 1) + n
