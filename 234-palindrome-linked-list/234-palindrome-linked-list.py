# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast , slow = head, head
        
    #Finding the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
    #Reverse second half
        Prev = None
        while slow:
            tmp = slow.next
            slow.next = Prev
            Prev = slow
            slow = tmp
            
    #Checking Palindrome
        left , right = head, Prev
        while right:
            if left.val!=right.val:
                return False
            left = left.next
            right = right.next
        return True