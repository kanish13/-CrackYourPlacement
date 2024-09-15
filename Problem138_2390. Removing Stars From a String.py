class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for i in s:
            if st:
                if (i=="*" and st[-1].isalpha()) or (i.isalpha() and st[-1]=="*"):
                   st.pop()
                else:
                   st.append(i)
            else:
                st.append(i)
        return "".join(st)
                   
