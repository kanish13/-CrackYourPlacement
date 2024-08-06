class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            j=0
            c=0
            while i:
                if i%10>j:
                    j=i%10
                i=i//10
                c=c+1
            x=x+int(str(j)*c)
        return x
