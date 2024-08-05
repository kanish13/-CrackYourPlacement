#Function to push element x to the front of the deque.
def push_front_pf(dq,x):
    #code here
    dq.insert(0,x)
    

#Function to push element x to the back of the deque.
def push_back_pb(dq,x):
    #code here
    dq.append(x)
    
#Function to return element from front of the deque.
def front_dq(dq):
    #code here
    if dq:
        return dq[0]
    return -1
#Function to pop element from back of the deque.
def pop_back_ppb(dq):
    #code here
    if dq:
        return dq.pop()
    return -1
