# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2 = headA, headB
        while l1!=l2: # l1 is not equal to l2
            
# id case is for after reaching null the l1 next has to point another list's head 
            l1 = l1.next if l1 else headB
#Same for this one also
            l2 = l2.next if l2 else headA  
        return l1