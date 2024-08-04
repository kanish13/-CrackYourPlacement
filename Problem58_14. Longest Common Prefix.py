class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        S=""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i]==strs[-1][i]:
                S=S+strs[0][i]
            else:
                break
        return S
