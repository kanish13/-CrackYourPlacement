class MyStack:

    def __init__(self):
        self.s=[]

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        if self.s:
            return self.s.pop()

    def top(self) -> int:
        if self.s:
            return self.s[-1]

    def empty(self) -> bool:
        if self.s:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
