class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s1=float("inf")
        s2=float("inf")
        b1=float("-inf")
        b2=float("-inf")

        for i in nums:

            if i>b1:
                t=b1
                b1=i
                b2=t
            else:
                if i>b2:
                    b2=i
            if i<s1:
                t=s1
                s1=i
                s2=t
            else:
                if i<s2:
                    s2=i
        return (b1*b2)-(s1*s2)
