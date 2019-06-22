# -*- coding:utf-8 -*-
"""
Q: 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。

A: 左右子树分治，中序遍历，递归实现。
根据二叉搜索树的的特点，根节点的左边连接左子树最右边的节点，
根节点的右边连接右子树最左边的节点。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        '''

        :param pRootOfTree:
        :return:
        '''
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # 左右分治
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        if left:
            while left.right:
                left = left.right

            pRootOfTree.left = left
            left.right = pRootOfTree

        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left

            pRootOfTree.right = right
            right.left = pRootOfTree

        # 赋予条件，左子树先处理完
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree