# -*- coding:utf-8 -*-
"""
Q: 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

A: 递归，在遍历每个节点的时候，记录它的深度，就可以一边遍历一边判断。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = True

    def IsBalanceTree(self, pRoot):
        # 记录每个节点深度, 最后返回flag
        self.getDepth(pRoot)
        return self.flag

    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left) + 1
        right = self.getDepth(root.right) + 1

        if abs(left - right) > 1:
            self.flag = False

        return max(left, right)
