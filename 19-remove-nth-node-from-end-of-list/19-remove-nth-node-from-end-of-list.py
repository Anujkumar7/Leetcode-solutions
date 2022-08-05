# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0,head)
        fast = start
        slow = start
        
        for i in range (n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return start.next