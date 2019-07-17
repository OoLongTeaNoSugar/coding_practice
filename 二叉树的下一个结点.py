# -*- coding:utf-8 -*-
"""
Q: 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

A: 三种情况：当前节点有右子树的话，当前节点的下一个结点是右子树中的最左子节点；
当前节点无右子树但是是父节点的左子节点，下一个节点是当前结点的父节点；
当前节点无右子树而且是父节点的右子节点，则一直向上遍历，直到找到最靠近的一个祖先节点pNode，pNode是其父节点的左子节点，
那么输入节点的下一个结点就是pNode的父节点。
"""
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        pNext = None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            pNext = pNode

        else:
            if pNode.next and pNode.next.left == pNode:
                pNext = pNode.next
            elif pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
                # 遍历终止时当前节点有父节点, 说明当前节点是父节点的左子节点, 输入节点的下一个结点为当前节点的父节点
                # 反之终止时当前节点没有父节点, 说明当前节点在位于根节点的右子树, 没有下一个结点    
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next

                if pNode.next:
                    pNext = pNode.next

        return pNext