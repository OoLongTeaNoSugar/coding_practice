# -*- coding:utf-8 -*-
# ######################
def S2ManacherStr(s):
    """
    :param s: ‘1221’
    :return:  ‘#1#2#2#2#1#’
    """
    man_s = '#'
    for i in s:
        man_s += i
        man_s += '#'
    return man_s

def Manacher(s):
    """
    回文半径数组
    :param s:
    :return: 最大回文长度
    """
    sm = S2ManacherStr(s)
    C = -1
    R = -1
    max_len = 0
    Parr = [0] * len(sm) # 回文半径数组
    for i in range(len(sm)):
        Parr[i] = min(Parr[2*C-i], R-i) if R > i else 1
        # i 在边界外， 扩边界
        while i + Parr[i] < len(sm) and i - Parr[i] > -1: # 确认 是否越过最前面一个数字
            if sm[i+Parr[i]] == sm[i-Parr[i]]:
                Parr[i] +=1
            else:
                break
        if i + Parr[i] > R:
            R = i + Parr[i]
            C = i
        max_len = max(max_len, Parr[i])

    # return max_len-1
    return Parr
if __name__ == "__main__":
    s= ['a', 'b']
    d = set(s) # hash set
    print(d)