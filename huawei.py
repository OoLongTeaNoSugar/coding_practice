# -*- coding:utf-8 -*-
# import sys
# line = sys.stdin.readline().strip().split("@")
# #print(line)
#
# s = line[0].strip().split(",")
# t = line[1].strip().split(",")

# print(t)
# def con(s,t):
#     dic = {}
#     res = ''
#     if len(t) == 0:
#         return s
#     for i in range(len(t)):
#         a = t[i].strip().split(":")
#         if a[0] not in dic.keys():
#             dic[a[0]] = int(a[1])
#         # print(dic)
#     for j in range(len(s)):
#         b = s[j].strip().split(":")
#         # print(b)
#         if b[0] not in dic.keys():
#             res += s[j]
#             res += ','
#         else:
#             res = res + b[0]+':'+str(int(b[1])-dic[b[0]]) + ','
#     return res[:-1]
# print(con(s,t))

def fun(arr):
    bonus = [1]* len(arr)
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            bonus[i] = bonus[i-1] + 1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > arr[i+1] and bonus[i] < bonus[i+1]+1:
            bonus[i] = bonus[i+1] + 1
    res = sum(bonus)
    return res
if __name__ == "__main__":
    import sys
    # n = int(input())
    # arr = [0]* n
    # for i in range(n):
    #     arr[i] = int(input())
    # print(fun(arr))
