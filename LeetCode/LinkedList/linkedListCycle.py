'''
LeetCode 141
Difficulty: Easy

https://leetcode.com/problems/linked-list-cycle/
----------------------------------------
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        curr = head
        while curr:
            if curr in s:
                return True
            else:
                s.add(curr)
            curr = curr.next
        
        return False