# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = "", ""
        while l1:
            n1 += str(l1.val)
            l1 = l1.next

        while l2:
            n2 += str(l2.val)
            l2 = l2.next

        total = int(n1[::-1]) + int(n2[::-1])
        reverse_and_string = str(total)[::-1]

        dummy = ListNode(0)
        res = dummy
        for n in reverse_and_string:
            node = ListNode(int(n))
            dummy.next = node
            dummy = dummy.next

        return res.next
