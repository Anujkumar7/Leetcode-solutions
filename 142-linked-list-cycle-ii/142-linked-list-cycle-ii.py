# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, entry, fast = head, head, head
        
        if head == None or head.next is None:
            return None
        
        while fast.next!= None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow== fast:  #There is a cycle
                while slow!=entry:  #Found the entry location
                    slow = slow.next
                    entry = entry.next
                return entry
        return None
        
        