class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=set()
        for i in emails:
            f=0
            st=""
            for j in range(len(i)):
                if "@" in st and (i[j]=="." or i[j]=="+"):
                    st=st+i[j]
                if i[j]=='+':
                    f=1
                elif i[j]=="@":
                    f=0
                    st=st+i[j]
                elif i[j].islower() and f==0:
                    st=st+i[j]
                
            s.add(st)
        return len(s)



                

