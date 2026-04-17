# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        res = False
        while cur:
            if cur not in seen:
                seen.add(cur)
            else:
                return True
            cur = cur.next
        return res
