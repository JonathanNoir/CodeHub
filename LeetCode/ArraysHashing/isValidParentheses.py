"""
LeetCode 20
Difficulty: Easy

https://leetcode.com/problems/valid-parentheses/description/
----------------------------------------

Example 1:
Input: s = "()"
Output: true


Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "("
Output: false

Example 5:
Input: s = "]"
Output: false

Example 6:
Input: s = "([{}])"
Output: true
----------------------------------------

Ref:
1. Using Data Structure:Stack and pop()
"""


class Solution:
    def isValid(self, s: str) -> bool:
        
        charmap = {'(' : ')' , '[' : ']', '{' : '}'}
        open_bracket = []

        for c in s:
            if c in charmap:
                open_bracket.append(c)
            else:
                if open_bracket:
                    if c != charmap[open_bracket.pop()]:
                        return False
                else:
                    return False
                
        if open_bracket:
            return False
        else:
            return True