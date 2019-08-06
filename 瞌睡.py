# -*- coding:utf-8 -*-
"""
链接：https://www.nowcoder.com/questionTerminal/93f2c11daeaf45959bb47e7894047085
来源：牛客网

小易觉得高数课太无聊了，决定睡觉。
不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。
你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，
你可以叫醒他一次，这会使得他在接下来的k分钟内保持清醒。
你需要选择一种方案最大化小易这堂课听到的知识点分值。
"""
import sys
n, k = map(int, sys.stdin.readline().split())
ai = map(int, sys.stdin.readline().split())
ti = map(int, sys.stdin.readline().split())
score = 0
for i in range(n):
    if ti[i] == 1:
        score += ai[i]

max_wake = 0
for i in range(k):
    if ti[i] == 0:
        max_wake += ai[i]
temp = max_wake
for j in range(n-k):
    if ti[j] == 0:
        temp -= ai[j]
    if ti[j+k] == 0:
        temp += ai[j+k]
    max_wake = max(max_wake, temp)
print(score+max_wake)