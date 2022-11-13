'''
LeetCode 206
Difficulty: Easy

https://leetcode.com/problems/reverse-linked-list/
----------------------------------------
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr            
            curr = tmp
            
        
        return prev

"""
Simulation:
Ex: 1 -> 2 -> 3 -> 4 -> 5

# prev = None
# curr = head => 1

LOOP=>1st:
  tmp = curr.next => 2
  curr.next = prev => None
  prev = curr => 1
  curr = tmp => 2

# prev = 1
# curr = 2

LOOP=>2nd:
  # Begin with CURR first
  # Get Next from CURR to var
  tmp = curr.next => 3

  # Since Next is got, setting Next to PREV(namely, reverse the pointer)
  curr.next = prev => 1

  # CURR are all settled
  # Now, Setting PREV, move it to the next node "of the PREV", which is CURR(that's why we can't move CURR first.)
  prev = curr => 2

  # Finally, setting CURR, move it to the next node
  curr = tmp => 3

prev = 2
curr = 3
"""