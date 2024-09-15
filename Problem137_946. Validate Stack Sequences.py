class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        j=0
        for i in pushed:
            st.append(i)
            while j<len(popped) and st and st[-1]==popped[j]:
                st.pop()
                j=j+1
        if not st:
            return True
        return False
