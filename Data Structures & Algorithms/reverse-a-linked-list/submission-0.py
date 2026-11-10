# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head, the node ur standing on
        # head.next, the rest of the list

        if not head:
            # edge case where head does not exist, empty list
            return None
        
        newHead = head
        if head.next:
            # if the next head exist, last iteration would be the second last node
            newHead = self.reverseList(head.next)
            # last iteration returns last node
            head.next.next = head
            # sets the last node pointing to the second last
        # cleaning up node so it doesn't go in a circle
        head.next = None

        # returns last node when we run reverList with only 1 length
        return newHead


            
        