# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        first = head
        while head:
            head = head.next
            count += 1

        n = count - n
        head = first

        if n == 0:
            if head:
                return head.next
            else:
                return None
        
        for i in range(n-1):
            head = head.next
        breakpoint = head
        reconnect = head.next.next
        breakpoint.next = reconnect
        return first

            

