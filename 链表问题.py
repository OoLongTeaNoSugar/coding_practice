# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class PalindromeList:
    """
    判断一个单链表是否为回文结构， 额外空间 O(1)的
    """
    def chkPalindrome(self, A):
        # write code here
        if A is None:
            return False
        if A.next is None:
            return True
        # 快慢指针找到中点
        head = A
        slow = A
        quick = A
        while True:
            quick = quick.next.next
            if quick is None:
                flag = 0
                break
            if quick.next is None:
                flag = 1
                slow = slow.next
                break
            slow = slow.next
        mid = slow

        # 改变链表结构 1->2->3->2->1  ==>  1->2->3<-2<-1
        start = mid.next
        cur = start

        tmp = cur.next
        while tmp is not None:
            after = tmp.next
            tmp.next = cur
            cur = tmp
            tmp = after

        res = (head.val == cur.val)
        tmp = cur.next

        # 两头遍历，并改回结构
        while cur != start:
            res = (cur.val == head.val and res)
            head = head.next
            after = tmp.next
            tmp.next = cur
            cur = tmp
            tmp = after

        return res

if __name__ == "__main__":
    test1 = [1,2,3,2,1]
    test2 = [1,2,3,1,4]

    l1 = ListNode(test1[0])
    l2 = ListNode(test2[0])

    for i in range(1, len(test1)):
        l1.next = ListNode(test1[i])
        l1 = l1.next
    for j in range(1, len(test2)):
        l2.next = ListNode(test2[j])
        l2 = l2.next

    l1 = ListNode(test1[0])
    l2 = ListNode(test2[0])

    # print(PalindromeList().chkPalindrome(l1))
    # print(PalindromeList().chkPalindrome(l2))
    print(l1.next.val)