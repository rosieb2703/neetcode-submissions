# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        mp = {}
        current = head

        while current:
            if current not in mp:
                mp[current] = "T"
                current = current.next
            else:
                return True
        
        return False
            

        