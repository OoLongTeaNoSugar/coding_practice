# -*- coding:utf-8 -*-
"""
得到最长子串
"""
def GetNextArray(string):
    next_arr = [0] * len(string)
    next_arr[0] = -1
    next_arr[1] = 0
    cn = 0
    i = 2
    while i < len(string):
        if string[i-1] == string[cn]:
            cn += 1
            next_arr[i] = cn
            i += 1
        elif cn > 0:
            cn = next_arr[cn]
        else:
            next_arr[i] = 0
            i += 1
    return next_arr

def GetIndexofStr1(str1, str2):
    """
    寻找str2是否是str1的字串算法
    :param str1:
    :param str2:
    :return: 返回的是str1和str2开始相同的位置， 否则返回-1
    """
    next_arr = GetNextArray(str2)
    i1, i2 = 0, 0
    while i1 < len(str1) and i2 < len(str2):
        if str1[i1] == str2[i2]:
            i1 += 1
            i2 += 1
        elif next_arr[i2] == -1:
            i1 += 1
        else:
            i2 = next_arr[i2]
    return i1 - i2 if i2 == len(str2) else -1

if __name__ == '__main__':
    import sys
    str1 = input() # 纯str操作时使用input()
    str2 = input()
    print(GetIndexofStr1(str1, str2))