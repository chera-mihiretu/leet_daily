# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode(0, head)

        prev = dummy 
        curr = dummy.next

        while curr and curr.next:
            hold = curr.next
            curr.next = curr.next.next
            hold.next = curr

            prev.next = hold 

            prev = prev.next.next
            curr = prev.next
        return dummy.next


            
            

