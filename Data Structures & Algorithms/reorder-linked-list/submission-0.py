# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next 
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        left = slow.next
        prev = slow.next = None
        while left : 
            temp = left.next
            left.next = prev  
            prev = left 
            left = temp 
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

            
        