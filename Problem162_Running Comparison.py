t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c=0
    for i in range(n):
        if a[i]<=b[i] and a[i]*2>=b[i]:
            c=c+1
        elif b[i]<=a[i] and b[i]*2>=a[i]:
            c=c+1
    print(c)
    t -= 1
