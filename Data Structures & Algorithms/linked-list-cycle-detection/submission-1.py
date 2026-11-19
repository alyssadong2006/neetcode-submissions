# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
            
        seen = []
        current = head
        while current.next:
            print(f"Current: {current.val}")
            if current not in seen:
                seen.append(current)
            else:
                return True

            current = current.next
        
        return False
        
        