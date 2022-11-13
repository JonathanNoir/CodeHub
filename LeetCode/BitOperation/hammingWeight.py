'''
LeetCode 191
Difficulty: Easy

https://leetcode.com/problems/number-of-1-bits/
----------------------------------------
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3

Example 2:
Input: n = 11111111111111111111111111111101
Output: 31

'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1
        
        return count

# Notes:
# 1 & 0 = 0 (False)
# 0 & 0 = 0 (False)
# 0 & 1 = 0 (False)
# 1 & 1 = 1 (True)

# Ex:
# 10111 ==> 23  #print(f"In binary: {23:b}")
# 00001 ==> 1

# after & operation :
# 00001 ==> 1

# 10111 >> 1 ==> 01011
