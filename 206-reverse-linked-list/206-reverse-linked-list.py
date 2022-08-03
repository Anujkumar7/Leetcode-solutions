# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,  head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        smallHead = self.reverseList(head.next)
        curr = smallHead
        while curr.next is not None:
            curr = curr.next
        curr.next = head
        head.next = None
        return smallHead
      
    