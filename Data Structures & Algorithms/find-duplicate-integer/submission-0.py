# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for n in nums:

            if n in s:
                return n
            else:
                s.add(n)

        return -1
