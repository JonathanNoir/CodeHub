'''
LeetCode 21
Difficulty: Easy

https://leetcode.com/problems/merge-two-sorted-lists/
----------------------------------------
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev_head = ListNode()
        tail=prev_head

        while list1 and list2 :
            if list1.val <= list2.val:
                tail.next = list1  #update list1 node inside NEXT to the new node
                list1 = list1.next #move (focused)node to the next in the list1 since it's used
            else:
                tail.next = list2 
                list2 = list2.next
            tail = tail.next #move tail node to the new node, for update its NEXT on next LOOP.

        #Handle if 2 list SIZE is different. Setting tail to the rest of bigger list
        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
        
        #prev_head.next is point to the first ListNode which is set in the first LOOP
        return prev_head.next

#Notes:Call by Value
#When Two Variable are point to the same Object
#Update Object's Attribute by either one Variable can affect both Variables
#Object is mutable
