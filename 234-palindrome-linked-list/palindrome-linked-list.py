# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        mid = fast = head

        while(fast != None and fast.next != None):
            mid = mid.next
            fast = fast.next.next

        first = head
        prev = None
        curr = head

        while(curr != mid):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        if fast:
            mid = mid.next

        while(prev != None and mid != None):
            if(prev.val != mid.val):
                return False
            prev = prev.next
            mid = mid.next
        
        return True

        
        