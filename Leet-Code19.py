# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 1 and not head.next:
            return None
        c = 0
        h1 = head
        h2 = head
        while c <n:
            h1 = h1.next
            c +=1
            if not h1:
                if c == n:
                    return head.next
                else:
                    return None
        while h1.next:
            h1 = h1.next
            h2 = h2.next
        h2.next = h2.next.next
        return head
