class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=[]
        y = [[] for _ in range(len(nums)+1)]
        c={}
        for i in nums:
            c[i]=c.get(i,0)+1
        for i,j in c.items():
            y[j].append(i)
        for i in y[::-1]:
            if i!=[]:
                for j in i:
                    if k>0:
                        x.append(j)
                        k=k-1
        return x

        
