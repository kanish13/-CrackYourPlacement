class TwoStacks:
    def __init__(self):
        self.s=[[],[]]

    # Function to push an integer into stack 1
    def push1(self, x):
        self.s[0].append(x)
    

    # Function to push an integer into stack 2
    def push2(self, x):
        self.s[1].append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.s[0]:
            return self.s[0].pop()
        else:
             return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.s[1]:
            return self.s[1].pop()
        else:
             return -1
