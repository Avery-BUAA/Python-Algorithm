# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        res1 = []
        res2 = []
        while curA != None:
            res1.append(curA)
            curA = curA.next
        while curB != None:
            res2.append(curA)
            curB = curB.next
        for i in res1:
            if i in res2:
                return True
        return False