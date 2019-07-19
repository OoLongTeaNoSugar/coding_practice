# -*- coding:utf-8 -*-
"""
Q: 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
 {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

A: 滑动窗口应当是队列，但为了得到滑动窗口的最大值，队列序可以从两端删除元素，因此使用双端队列。
对新来的元素k，将其与双端队列中的元素相比较，
前面比k小的，直接移出队列（因为不再可能成为后面滑动窗口的最大值了!）,
前面比k大的X，比较两者下标，判断X是否已不在窗口之内，不在了，直接移出队列，队列的第一个元素是滑动窗口中的最大值。
"""
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size <= 0:
            return []
        deque = []
        if len(num) >= size:
            index = []
            for i in range(size): # 初始窗口
                # 前面比num[i]小的，直接移出队列（因为不再可能成为后面滑动窗口的最大值了!）,
                # while：比较全部
                while len(index) > 0 and num[i] > num[index[-1]]:
                    index.pop()
                index.append(i)

            for i in range(size, len(num)): # 窗口往后移动
                # 先加入上个窗口的最大值
                deque.append(num[index[0]])
                # 同样的规则执行
                while len(index) > 0 and num[i] >= num[index[-1]]:
                    index.pop()
                # 判断X是否已不在窗口之内，不在了，直接移出队列
                if len(index) > 0 and index[0] <= i - size:
                    index.pop(0)
                index.append(i)

            deque.append(num[index[0]]) # 加入最后一个窗口的最大值
        return deque