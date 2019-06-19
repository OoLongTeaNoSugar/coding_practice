# -*- coding:utf-8 -*-
"""
Q: 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

A: 根据后序遍历的特点，尾元素一定是根节点，
同时小于尾元素的值时左子树，大于尾元素的值时右子树。
且序列前半部分小于尾元素，后半部分大于尾元素，
可以将序列划分为左子树序列和右子树序列，然后递归。
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False

        lenth = len(sequence)
        # 尾元素为根节点
        root = sequence[-1]

        for i in range(lenth):
            # sequence中大于尾元素的为右子树
            # i停止计数
            if sequence[i] > root:
                break

        for j in range(i, lenth):
            # j从上面i停止的地方开始，如果有小于root的节点，则说明右子树错误
            if sequence[j] < root:
                return False

        left = True
        if i > 0 :
            # 检查左子树的子树是否后序遍历
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if j < lenth - 1:
            right = self.VerifySquenceOfBST(sequence[i:lenth - 1])

        return left and right


