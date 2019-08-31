# -*- coding:utf-8 -*-

"""
给一个arr，求出现次数最多的topk个
"""

import heapq
def printTopKAndRank(string, topK):
    if not string or len(string) == 0 or topK < 1:
        return
    smap = {} # 建立一张hashmap，统计词频
    for i in string:
        if not (i in smap):
            smap[i] = 0
        smap[i] += 1

    topK = min(len(string), topK)
    heap = []
    for key in smap.keys():
        heap.append([key, smap[key]])
    heapq.heapify(heap)
    return heapq.nlargest(topK, heap, key=lambda x:x[1])

if __name__ == "__main__":
    s = "abaabbccddeeffgg"
    topk = 2
    print(printTopKAndRank(s, topk)) # [['a', 3], ['b', 3]]