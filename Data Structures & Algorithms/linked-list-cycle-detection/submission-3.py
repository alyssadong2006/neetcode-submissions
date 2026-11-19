# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        # use set whnever you care about:
        # - is X in here?
        # - give me only distinct items
        # (a set has no order or duplicates)
        seen = set()
        current = head

        while current:
            if current not in seen:
                seen.add(current)
            else:
                return True
            current = current.next
        
        return False
        