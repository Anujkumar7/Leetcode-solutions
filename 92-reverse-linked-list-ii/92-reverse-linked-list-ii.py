# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
#  Reach node at position left

        leftPrev, curr = dummy,head
        for i in range (left-1):
            leftPrev,curr = curr,curr.next
#Now curr = "left", leftPrev="node before left"
#  Reverse from left to right
        prev = None
        for i in range(right-left+1):
            tmpNext = curr.next
            curr.next = prev
            prev,curr = curr,tmpNext
# Update Pointers
        leftPrev.next.next=curr #Cur is node after "Right"
        leftPrev.next = prev  #Prev is "Right"
        return dummy.next