"""
LeetCode 242
Difficulty: Easy

https://leetcode.com/problems/valid-anagram/
----------------------------------------

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))
        return s1 == t1