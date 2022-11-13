'''
LeetCode 338
Difficulty: Easy

https://leetcode.com/problems/counting-bits/
----------------------------------------
Example 1:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

----------------------------------------
Notes:
1. Using F-String to get binary:
    print(f'{5:b}') ==> 101
    print(f'{4:b}') ==> 100

2. Using Counter to count number of '1'
    c=Counter('101')
    c['1']          ==> 2
    c.items()       ==> dict_items([('1', 2), ('0', 1)])

3. Split a string into a Python list using unpack(*) method
    string = "geeks"
    li = [*string]   ==> ['g', 'e', 'e', 'k', 's']

    l2 = list(string) ==> ['g', 'e', 'e', 'k', 's']
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        from collections import Counter
        
        return [Counter(f"{i:b}")['1'] for i in range(n+1)]

#Solution 2: Without using built-in function
class Solution2:
    def countBits(self, n: int) -> List[int]:
        list_binary = [f"{i:b}" for i in range(n+1)]
        
        '''
        Ex: 101 => 1+0+1 =2
        '''
        res=[]        
        for item in list_binary:
            res.append(sum([int(i) for i in [*item]]))
        
        return res