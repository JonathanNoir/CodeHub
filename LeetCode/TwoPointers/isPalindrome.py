'''
LeetCode 125
Difficulty: Easy
----------------------------------------

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

----------------------------------------
Ref:
str.isalnum()
str.isalpha()
str.isdigit()

#Get ascii number:
ord('a')
ord('A')
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha=''.join(char for char in s if char.isalnum())
        
        l,r = 0,len(s_alpha)-1
        
        while l < r:
            if s_alpha[l].lower() != s_alpha[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

