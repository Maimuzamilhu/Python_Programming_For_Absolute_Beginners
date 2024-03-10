"""Longest String without Repeating Characters
Input = abcabcbb
output = 3
"""

class Solution:
    def longeststring(self , s):
        charset = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in charset: 
                charset.remove(s[left]) #if right char already have in set then remove the left char and add left+1
                left+=1

            charset.add(s[right])
            res = max(res , right - left +1) #update the max result

        return res
