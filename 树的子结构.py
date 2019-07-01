# -*- coding:utf-8 -*-
"""
Q: 输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）

A: 在树A中查找和树B根节点一致的值，
然后判断树A中以该节点为根节点的子树，
是不是和树B有相同的结构。可以通过递归实现。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        '''

        :param pRoot1:
        :param pRoot2:
        :return:bool
        '''
        res = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                res = self.IfTree1hasTree2(pRoot1, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.right, pRoot2)

        return res

    def IfTree1hasTree2(self, pRoot1, pRoot2):
        '''

        :param pRoot1:
        :param pRoot2:
        :return: bool
        '''

        # 修改错误，B树为空时，表示全部对比完毕，均为正确输出yes
        if pRoot2 == None:
            return True

        # B树不为空，但是A树为空代表子树不相同，输出false
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.IfTree1hasTree2(pRoot1.left, pRoot2.left) and self.IfTree1hasTree2(pRoot1.right, pRoot2.right)
