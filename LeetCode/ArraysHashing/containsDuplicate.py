"""
LeetCode 217
Difficulty: Easy

https://leetcode.com/problems/contains-duplicate/
----------------------------------------

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        
        counters = Counter(nums)
        res = counters.most_common(1)
        return res[0][1] > 1

