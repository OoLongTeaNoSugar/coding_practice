# -*- coding:utf-8 -*-
"""
Q: 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)

A: 用前序遍历的方式访问二叉树的节点，当访问到一个节点时，将该节点加到路径中，并累加节点的值。
直到访问到符合要求的节点或者访问到叶节点，然后递归访问该节点的父节点，
在函数退出时要删除当前节点，并减去当前节点的值。
实际上是一个出栈和入栈的过程。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        '''
        :param root:根节点
        :param expectNumber:整数
        :return: result：list
        '''

        if not root or root.val > expectNumber:
            # 边界条件，根节点为空，或根节点值大于整数值
            return []

        if not root.left and not root.right and root.val == expectNumber:
            # 根节点无子树，且根节点值恰好是整数值
            return [[root.val]]
        else:
            # 整数先减去根节点值
            expectNumber -= root.val
            left = self.FindPath(root.left, expectNumber)
            right = self.FindPath(root.right, expectNumber)

            result = [[root.val]+i for i in left]
            for i in right:
                result.append([root.val]+i)

        return sorted(result, key=lambda x:-len(x))


