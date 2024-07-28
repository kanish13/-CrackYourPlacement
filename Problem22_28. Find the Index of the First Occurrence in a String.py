# 28. Find the Index of the First Occurrence in a String. Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Solution :

class Solution:
    def strStr(self, x: str, y: str) -> int:
        if len(y)>len(x):
            return -1
        for i in range(len(x)):
            if x[i:i+len(y)]==y:
                return i
        return -1
