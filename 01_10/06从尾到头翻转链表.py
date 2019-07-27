
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
#Definition for singly-linked list.
#1.先记录下一个节点，不然cur的next等于pre后，cur就找不到下一个节点了。
#2.当前节点的下一个等于pre
#3.让pre=当前节点
#4.cur =tep 即cur到下一个节点
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur = head
        pre = None
        while cur != None:
            tep =cur
            cur.next = pre
            pre = tep
            cur = cur.next
        return cur


