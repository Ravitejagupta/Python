# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd1 = head
        even1 = head.next
        odd = head
        even = head.next
        while odd.next and even:
            odd.next = even.next
            if odd.next:
                odd = odd.next
            else:
                break
            even.next = odd.next
            even = even.next
        odd.next = even1
        return odd1
            
