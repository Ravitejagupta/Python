# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = d1 = ListNode(0)
        h2 = d2 = ListNode(0)
        while head:
            if head.val < x:
                d1.next = head
                d1 = d1.next
            else:
                d2.next = head
                d2 = d2.next
            head = head.next
        d2.next = None
        d1.next = h2.next
        return h1.next
