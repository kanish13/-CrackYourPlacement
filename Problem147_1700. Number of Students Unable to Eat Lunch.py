class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ss={1:0,0:0}
        r=len(students)
        for i in students:
            ss[i]=ss.get(i,0)+1
        
        for i in sandwiches:
            if ss[i]>0:
                ss[i]=ss[i]-1
                r=r-1
            else:
                return r
        return r
            
