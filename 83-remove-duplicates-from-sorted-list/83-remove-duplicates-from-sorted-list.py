# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        while start:
            while start.next and start.val == start.next.val:
                start.next =start.next.next
            start = start.next
        return head