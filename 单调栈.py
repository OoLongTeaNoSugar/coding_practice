# -*- coding:utf-8 -*-
"""
单调栈 取得离该位置最近的比其小的数
"""
def getnearlessmin(array):
    """
    :param array: 原始数组
    :return: res[i][0] i位置的数， 左边离i最近， 比arr[i]小的数的位置
             res[i][1] i位置的数， 右边离i最近， 比arr[i]小的数的位置
    """
    stack = [] # 从小到大，如果找比其大的数，从大到小
    n = len(array)
    """
    ATTENTION!!!!!!!!!!!不要用浅拷贝！！！！ 
    """
    res = [[0, 0] for _ in range(n)]
    for i in range(n):
        # 先结算栈里面的答案
        while len(stack) != 0 and array[stack[-1][0]] < array[i]:
        # while len(stack) != 0 and array[stack[-1][0]] > array[i]:
            popIs = stack.pop()
            leftlessIndex = -1 if len(stack) == 0 else stack[-1][-1]
            for popi in popIs:
                res[popi][0] = leftlessIndex
                res[popi][1] = i

        # i 压栈
        if len(stack) != 0 and array[stack[-1][0]] == array[i]:
            stack[-1].append(i)
        else:
            lis = []
            lis.append(i)
            stack.append(lis)

    # 遍历结束，单独处理栈里面的元素
    while len(stack) != 0:
        popIs = stack.pop()
        leftlessIndex = -1 if len(stack) == 0 else stack[-1][-1]
        for popi in popIs:
            res[popi][0] = leftlessIndex
            res[popi][1] = -1

    return res


def nextIndex(n, i):
    if i < n - 1:  # 当最高山峰下标不是最后一个时，下一个下标直接加1
        return i + 1
    return 0  # 最高山峰下标是最后一个，下一个下标为0


def getInternalSum(n):  # 相同元素计算内部对数，组合数C(n,2)
    return (n * (n - 1)) / 2

def Sloution(array, n, maxindex):
    """
    https://www.nowcoder.com/questionTerminal/e1967ae812ea42e7a3ce57ee1f83b686?orderByHotValue=1&commentTags=Python
    """
    stack = [] # 从小到大，如果找比其大的数，从大到小[index, count]
    res = 0
    ind = nextIndex(n, maxindex)
    stack.append([maxindex, 1])
    while ind != maxindex:
        val = array[ind]
        # 先结算栈里面的答案
        while len(stack) != 0 and array[stack[-1][0]] < val:
            times = stack[-1][1]  # 记录栈顶元素的个数
            stack.pop()  # 栈顶元素出栈
            res += getInternalSum(times) + times  # 内部对数+它右边相邻的数能看到所有的该数
            if len(stack) > 0:  # 如果栈中还有元素，则它左边相邻的数也能看到所有的该数
                res += times
        # i 压栈
        if len(stack) != 0 and array[stack[-1][0]] == val:
            stack[-1][1] += 1
        else:
            stack.append([ind, 1])
        ind = nextIndex(n, ind)  # 下一个数

    # 遍历结束，单独处理栈里面的元素
    while len(stack) != 0:
        times = stack[-1][1]  # 栈顶元素的个数
        stack.pop()  # 栈顶元素出栈
        res += getInternalSum(times)  # 栈顶元素内部的对数
        if len(stack) > 0:  # 若它左边还有更大的数
            res += times  # 则相邻数能看到所有的该数
            if len(stack) > 1:  # 若左边比它大的元素不止一个值
                res += times  # 由于是环形，栈底元素也可看到所有的该值
            else:
                if stack[-1][1] > 1:  # 若左边相邻的数即为栈底元素，且个数大于1
                    res += times  # 由于是环形，则另一端也可看到所有的该值
    return int(res)

if __name__ == "__main__":
    test = [1,2,4,5,3]
    n = len(test)
    maxval = max(test)
    maxindex = test.index(maxval)
    print(Sloution(test, n, maxindex))