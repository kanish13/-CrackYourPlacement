t = int(input())
d={'00':"A",'01':"T",'10':"C",'11':"G"}

while t > 0:
    n = int(input())
    s = input()
    # Your code goes here
    l=0
    r=1
    res=""
    while r<n:
        res=res+d[s[l]+s[r]]
        l=l+2
        r=r+2
    print(res)
    t -= 1

