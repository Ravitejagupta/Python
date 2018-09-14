# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = {}
        a = head
        r = dummy = ListNode(0)
        while a:
            if a.val in d:
                d[a.val] += 1
            else:
                d[a.val] = 1
            a = a.next
        a = head
        while a:
            if d[a.val] == 1:
                dummy.next = a
                dummy = dummy.next
            a = a.next
        dummy.next = None
        return r.next
