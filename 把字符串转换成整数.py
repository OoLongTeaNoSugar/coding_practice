# -*- coding:utf-8 -*-
"""
Q: 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

A: 主要是区分输入和合法性，比如输入一个None，输入一个空字符串 “ ”，
或者输入的字符串中含有“+”或者“-”，或者输入的字符串中含有除去“+”“-” 数字的非数字字符。
"""
class Solution:
    def Str2Int(self, s):
        # 处理边界
        if not s or len(s) < 1:
            return 0

        num = [] # 记录每一位数字
        # 建立对应字典
        numDict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        for i in s:
            if i in numDict.keys():
                num.append(numDict[i])
            elif i == '-' or i == '+':
                continue
            else:
                return 0

        ans = 0 # 数位相加之和
        if len(num) == 1 and num[0] == 0:
            return 0
        for i in num:
            ans = ans*10 + i
        if s[0] == '-': # 符号处理
            ans = 0 - ans
        return ans
