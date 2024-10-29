class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if nums:
            i=nums[0]
            j=nums[0]
            
    
            for x in range(1,len(nums)):
                if nums[x]==j+1:
                    j=nums[x]
                elif i==j:
                    res.append(str(i))
                    i=nums[x]
                    j=nums[x]
                else :
                    res.append(str(i)+"->"+str(j))
                    i=nums[x]
                    j=nums[x]
            if i==j:
                res.append(str(i))
            else :
                res.append(str(i)+"->"+str(j))

        return res
