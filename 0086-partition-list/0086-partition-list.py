# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_big = ListNode(-1)
        dummy_small = ListNode(-1)
        curr1, curr2 = dummy_big, dummy_small
        while head:
            if head.val >= x:
                curr1.next = head
                curr1 = curr1.next
            else:
                curr2.next = head
                curr2 = curr2.next
            head = head.next
        curr2.next = dummy_big.next
        curr1.next = None

        return dummy_small.next