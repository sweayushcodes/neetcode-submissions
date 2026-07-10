# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle 
        slow = fast = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        # cleanly separate first & second part
        second = slow.next
        slow.next = None
        # reverse the second part
        prev = None
        curr = second
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # merge per the given constraints
        first = head
        second = prev
        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
            

        