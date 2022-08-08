# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k==1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur ,nex ,pre = dummy ,dummy ,dummy
        count = 0
        i=k-1
        
        while cur.next!=None:
            cur = cur.next
            count+=1
        while count>=k:
            cur = pre.next
            nex = cur.next
            for i in range(i):
                i+=1
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            count-=k
        return dummy.next