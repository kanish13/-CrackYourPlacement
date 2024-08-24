class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=""
        for i in s[::-1]:
            if i==" " and x!="":
                return len(x)
            elif i!=" ":
                x=x+i
        return len(x)
